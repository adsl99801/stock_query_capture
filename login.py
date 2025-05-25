import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import load_config
from selenium.webdriver.support.ui import Select

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
    page_id_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, config["input_pageIdNo"]))
    )
    page_id_input.send_keys(config["input_pageIdNo_value"])
    # 選擇 caType 下拉選單中的行動自然人憑證
    ca_type_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, config["select_caType"]))
    )
    ca_type_select_el = Select(ca_type_select)
    ca_type_select_el.select_by_value(config["select_caType_value"])

    button_nextStepBtn= WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, config["button_nextStepBtn"]))
    )
    button_nextStepBtn.click()
    print("正在將頁面捲動到底部...")
    driver.execute_script("const scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
    # 提示用戶完成登入並等待跳轉
    print("請在瀏覽器中完成登入（TW FidO），登入成功後應跳轉至初始頁面")
    print("跳轉後按 Enter 繼續...")
    WebDriverWait(driver, 60).until(
        EC.url_contains(config["redirect_url_contains"])  # 等待跳轉至初始頁面
    )
    # input()  # 等待用戶確認

