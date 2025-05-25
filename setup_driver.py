from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    try:
        service = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")  # 設置窗口大小
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"初始化 WebDriver 失敗：{e}")
        raise