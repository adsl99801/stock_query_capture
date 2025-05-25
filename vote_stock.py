import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import load_config
from extract_text import extract_text

def vote_page_all_a_notes(driver):
    try:
        config = load_config()
        a_votes = WebDriverWait(driver, 1).until(
            EC.presence_of_all_elements_located((By.XPATH, config["a_vote"]))
        )
        print(f"找到 {len(a_votes)} 個投票按鈕")
        return a_votes
    except Exception as e:
        print(f"無法找到投票按鈕：{e}")
        return []

def to_vote(driver, query_url, stock_info_page_num):
    """處理所有投票按鈕的投票流程"""
    index = 1
    while True:
        print(f"\n處理第 {index} 個投票按鈕")
        try:
            a_notes = vote_page_all_a_notes(driver)
            if not a_notes:
                print("未找到投票按鈕，結束處理")
                break
            if index > len(a_notes):
                print("所有投票按鈕已處理完畢")
                break
            
            a_note = a_notes[index - 1]
            to_vote_page(driver, a_note, query_url)
            index += 1
            
            # 返回原始頁面以繼續處理下一個投票按鈕
            driver.get(query_url)
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        except Exception as e:
            print(f"處理第 {index} 個投票按鈕時發生錯誤：{e}")
            break

def click_element(driver, xpath, description, timeout=1):
    """通用函數：嘗試查找並點擊元素 description == "a_approve_sure-機器人判斷"""
    try:
        config = load_config()
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        xpath_els = driver.find_elements(By.XPATH,xpath)
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(element))
        if driver.find_elements(By.XPATH,config["div_robot"]):
            print(f"div_robot")
        if description == "a_approve_sure":
            driver.execute_script("document.voteform.token.value = '123'")
        if description == "button_doProcess":
            driver.execute_script("document.voteform.token.value = '123'")
        xpath_els[-1].click()
        print(f"成功點擊{description}")
        div_votelist_actions = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, config["div_votelist_actions"]))
        )
        return True
    except Exception as e:
        print(f"未找到{description}：{e}")
        return False

def to_vote_page(driver, a_note, query_url):
    """執行單個投票按鈕的投票流程"""
    config = load_config()
    
    # 點擊投票按鈕
    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable(a_note))
        a_note.click()
        print("點 投票 進入畫面")
    except Exception as e:
        print(f"點 投票 進入畫面失敗：{e}")
        return

    filename = extract_text(driver)
    print(f"vote_stock.extract_text:{filename}")
    
    # 定義按鈕流程：按順序嘗試點擊
    button_steps = [
        (config["a_approve"], "a_approve"),
        (config["a_approve_next_button"], "a_approve_next_button"),
        # (config["input_checkAllCandidates"], "input_checkAllCandidates"),
        # (config["a_avarage"], "a_avarage"),
        (config["a_disapprove"], "a_disapprove"),
        (config["a_approve_next_button"], "a_approve_next_button"),
        (config["button_ignoreVote"], "button_ignoreVote"),
        (config["a_approve_next_button"], "a_approve_next_button")
    ]
    
    # 執行按鈕點擊流程
    
    while True:
        for xpath, description in button_steps[:]:
            if not click_element(driver, xpath, description):
                print(f"click_element失敗{description}")
        div_votelist_actions = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, config["div_votelist_actions"]))
        )
        if not driver.find_elements(By.XPATH,config["a_approve_next_button"]):
            # 沒有下一步了
            print(f"沒有下一步了{description}")
            break
    # 最後執行剩餘的按鈕
    final_steps = [
        (config["a_approve_sure"], "a_approve_sure"),
        (config["button_doProcess"], "button_doProcess"),
        (config["button_done"], "button_done")
    ]
    for xpath, description in final_steps:
        if click_element(driver, xpath, description):
            if description == "button_done":
                print(f"投票完成{description}")
                break
            else:
                print(f"click_element fail {description}")