from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid


def extract_text(driver):
    # 步驟 3：提取第一個 h2 元素的文字（僅取第一行並處理）
    try:
        h2_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )
        h2_text = h2_element.text.strip().split("\n")[0]  # 取第一行
        safe_filename = h2_text.split("貴股東對")[-1].strip()  # 按 "貴股東對" 分割並清理
        if not safe_filename:
            safe_filename = f"screenshot_{uuid.uuid4()}"
        print(f"提取的文字：{h2_text}")
        print(f"處理後的檔案名稱：{safe_filename}")
        return safe_filename
    except Exception as e:
        print(f"無法提取 h2 文字：{e}")
        safe_filename = f"screenshot_{uuid.uuid4()}"
        return safe_filename