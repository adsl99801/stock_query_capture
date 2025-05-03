from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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