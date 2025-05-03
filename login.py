import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import load_config


def perform_login(driver):
    # 載入參數
    config = load_config()

    # 步驟 0：開啟登入頁面，等待手動登入
    login_url = config["login_url"]
    print(f"正在開啟登入頁面：{login_url}")
    driver.get(login_url)

    # 等待頁面加載
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # 提示用戶完成登入並等待跳轉
    print("請在瀏覽器中完成登入（TW FidO），登入成功後應跳轉至初始頁面")
    print("跳轉後按 Enter 繼續...")
    WebDriverWait(driver, 60).until(
        EC.url_contains(config["redirect_url_contains"])  # 等待跳轉至初始頁面
    )
    input()  # 等待用戶確認

