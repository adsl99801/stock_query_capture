from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def setup_driver():
    # 設置 Chrome 選項
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速
    chrome_options.add_argument("--window-size=1920,1080")  # 設置窗口大小

    # 初始化 WebDriver
    try:
        chromedriver_path = r"D:\Users\keith\project\driver\chromedriver.exe"
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"初始化 WebDriver 失敗：{e}")
        print("請確保 ChromeDriver 134 版已安裝，且路徑 D:\\Users\\keith\\project\\driver\\chromedriver.exe 正確")
        raise