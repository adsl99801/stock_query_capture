from setup_driver import setup_driver
from login import perform_login
from click_query import get_query_buttons, click_query_button, capture_by_query
from extract_text import extract_text
from capture_screenshot import capture_screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import load_config
from vote_stock import to_vote, vote_page_all_a_notes

def main():
    try:
        # 步驟 0：初始化 WebDriver
        driver = setup_driver()

        # 步驟 1：登入
        perform_login(driver)

        # 步驟 2：從 config 載入 configuration
        config = load_config()
        base_query_buttons_url = config["query_buttons_url"]

        # 步驟 3：迴圈處理 stockInfo 每一頁，每家公司投票完就不會出現在第一頁
        stock_info_num = 1
        while stock_info_num <= 2:  # 全部投完後面的頁數不會有投票按鈕了
            query_buttons_url = f"{base_query_buttons_url}{stock_info_num}"
            print(f"正在處理頁面：{query_buttons_url}")

            # 步驟 3-1：檢查當前頁面是否有投票按鈕
            driver.get(query_buttons_url)
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # 檢查是否有未投票的按鈕
            a_votes = vote_page_all_a_notes(driver)
            if not a_votes:
                print(f"頁面 {stock_info_num} 已無未投票按鈕，跳到下一頁")
                stock_info_num += 1
                continue

            # 步驟 3-2：執行投票流程
            to_vote(driver, query_buttons_url, stock_info_num)

            # 再次檢查當前頁面是否還有未投票按鈕
            driver.get(query_buttons_url)
            WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            a_votes = vote_page_all_a_notes(driver)
            if not a_votes:
                print(f"頁面 {stock_info_num} 投票完成，跳到下一頁")
                stock_info_num += 1
            else:
                print(f"頁面 {stock_info_num} 仍有未投票按鈕，重新處理")
        # 步驟 4開始截圖
        stock_info_num = 2
        while stock_info_num <= 11:  # 看總要處理幾頁
            query_buttons_url = f"{base_query_buttons_url}{stock_info_num}"
            print(f"正在跳轉至截圖前初始頁面：{query_buttons_url}")
            driver.get(query_buttons_url)
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            # 步驟 6：進去該頁所有查詢按鈕並截圖
            capture_by_query(driver, query_buttons_url, stock_info_num)
            stock_info_num = stock_info_num + 1
    except Exception as e:
        print(f"執行過程中發生錯誤：{e}")

    # 不關閉瀏覽器
    print("腳本執行完畢，瀏覽器保持開啟")

if __name__ == "__main__":
    main()