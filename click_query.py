from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from extract_text import extract_text
from capture_screenshot import capture_screenshot
import os

def get_query_buttons(driver):
    # 獲取所有查詢按鈕
    try:
        buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[@class='c-actLink' and text()='查詢']"))
        )
        print(f"找到 {len(buttons)} 個查詢按鈕")
        return buttons
    except Exception as e:
        print(f"無法找到查詢按鈕：{e}")
        return []


def click_query_button(driver, button, query_buttons_url):
    # 點擊指定的查詢按鈕並等待目標頁面加載
    try:
        button.click()
        print("已點擊查詢按鈕")
    except Exception as e:
        print(f"點擊查詢按鈕失敗：{e}，嘗試直接導航至目標頁面")
        driver.get(query_buttons_url)

    # 等待目標頁面加載
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "stockInfo"))
    )

def capture_by_query(driver, query_url, stock_info_page):
    """Process each query button for a given stockInfo URL."""
    index = 1
    while True:
        print(f"\n處理第 {index} 個查詢按鈕 for stockInfo={stock_info_page}")
        try:
            # 步驟 4：獲取所有查詢按鈕
            query_buttons = get_query_buttons(driver)
            if not query_buttons:
                print(f"未找到任何查詢按鈕 for stockInfo={stock_info_page}，結束處理")
                break
            if index > len(query_buttons):
                print(f"所有查詢按鈕已處理完畢 for stockInfo={stock_info_page}")
                break
            print(f"process_query_buttons:{index}")
            # 步驟 5：點擊查詢按鈕
            button = query_buttons[index - 1]  # 獲取當前索引的按鈕
            click_query_button(driver, button,query_url)

            # 步驟 6：提取文字
            filename = extract_text(driver)

            output_dir = "./result"
            output_path = f"{output_dir}/{filename}.jpg"
            if os.path.exists(output_path):
                print(f"截圖已存在：{output_path}，跳過截圖")
            else:
                capture_screenshot(driver, filename, stock_info_page)

            # 返回初始頁面
            driver.get(query_url)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "stockInfo"))
            )
            index += 1
        except Exception as e:
            print(f"處理第 {index} 個查詢按鈕時發生錯誤 for stockInfo={stock_info_page}：{e}")
            break  # 或 continue，根據需求決定是否繼續