# 股票查詢與投票自動化腳本 (Stock Query Capture Script)

## 專案概述
本專案是一個基於 Python 的自動化腳本，專為與台灣集保結算所（TDCC, Taiwan Depository & Clearing Corporation）的股票服務網站交互而設計。該腳本實現了自動化登入、查詢按鈕點擊、文字提取、螢幕截圖以及投票流程自動化等功能，旨在讓股民於電子投票操作中提升效率並降低手動操作的錯誤風險。作為一名資深的架構分析師，我設計了模組化的架構，確保程式碼的可維護性、可擴展性和穩定性，並整合了錯誤處理和靈活的配置管理。

## 功能特性
- **自動化登入**：透過 Selenium WebDriver 開啟 TDCC 登入頁面，並支援手動 TW FidO 認證，確保安全性與靈活性。
- **查詢按鈕處理**：動態識別並點擊查詢按鈕，處理多頁股票資訊頁面。
- **文字提取**：從頁面的 `<h2>` 元素中提取文字，用於生成有意義的截圖檔案名稱，提升檔案管理效率。
- **螢幕截圖**：自動截取指定頁面區域並裁剪，保存為高品質 JPG 檔案，支援批量處理。
- **投票自動化**：自動化處理 TDCC 網站的投票流程，包括贊成、棄權等選項，確保投票結果準確無誤。
- **模組化設計**：將功能拆分為獨立模組（如登入、查詢、截圖、投票），便於維護和功能擴展。
- **靈活配置**：透過 JSON 配置文件管理 URL、XPath 和其他參數，適應網站結構變更。
- **錯誤處理**：全面的異常處理機制，確保腳本在網路不穩定或頁面結構變更時的穩定性。

## 技術棧
- **程式語言**：Python 3.8+
- **核心庫**：
  - **Selenium WebDriver**：用於瀏覽器自動化，支援動態網頁交互。
  - **Pillow**：用於螢幕截圖的裁剪和處理。
  - **webdriver-manager**：自動管理 ChromeDriver，簡化環境配置。
  - **JSON**：用於配置文件解析，實現參數化管理。
- **瀏覽器**：Google Chrome（相容 ChromeDriver 134 版）
- **其他工具**：Git（版本控制）

## 先決條件
- **環境要求**：
  - Python 3.8 或更高版本（透過 Conda 安裝）
  - Google Chrome 瀏覽器（相容 ChromeDriver 134 版）
  - ChromeDriver（版本 134，手動放置於 `D:\Users\XXX\project\driver\chromedriver.exe` 或根據環境調整）
- **Conda 環境**：建議使用 Conda 創建虛擬環境以管理依賴。

## 安裝步驟
1. **克隆專案**：
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **創建並啟用 Conda 環境**：
   ```bash
   conda create -n stock_query python=3.8
   conda activate stock_query
   ```

3. **安裝依賴**：
   使用 Conda 安裝所需的 Python 套件：
   ```bash
   conda install selenium pillow
   pip install webdriver-manager
   ```
   **注意**：`webdriver-manager` 目前在 Conda 的套件庫中可能不可用，因此使用 pip 安裝。請確保 Conda 環境已啟用。

4. **設置 ChromeDriver**：
   - 從 [ChromeDriver 官方網站](https://chromedriver.chromium.org/downloads) 下載版本 134。
   - 將 `chromedriver.exe` 放置於 `D:\Users\XXX\project\driver\chromedriver.exe`，或在 `setup_driver.py` 中更新路徑。

5. **配置 `config.json`**：
   - 確保專案根目錄下存在 `config.json`，並包含以下必要參數：
     ```json
     {
         "login_url": "https://stockservices.tdcc.com.tw/evote/login/goTwFidO.html",
         "query_buttons_url": "https://stockservices.tdcc.com.tw/evote/shareholder/000/tc_estock_welshas.html?stockInfo=",
         "redirect_url_contains": "tc_estock_welshas",
         "input_pageIdNo": "//input[@name=\"pageIdNo\"]",
         "input_pageIdNo_value": "XXXXXXXXXX",
         "select_caType": "//select[@name=\"caType\"]",
         "select_caType_value": "ST",
         "button_nextStepBtn": "//button[@name=\"nextStepBtn\"]"
     }
     ```
   - 根據實際需求更新 `input_pageIdNo_value` 等敏感資訊。

## 使用說明
1. **執行腳本**：
   ```bash
   conda activate stock_query
   python main.py
   ```

2. **操作流程**：
   - 腳本將開啟 Chrome 瀏覽器並導航至 TDCC 登入頁面。
   - 在瀏覽器中"手動"完成行動自然人或其他憑證認證（需在 60 秒內完成）。
   - 登入成功並跳轉至初始頁面後，按 **Enter** 鍵繼續執行。
   - 腳本將自動處理投票流程，點擊所有投票按鈕並完成投票。
   - 投票完成後，腳本將逐頁處理查詢按鈕並生成截圖，儲存至 `./result/` 目錄。

3. **輸出**：
   - 截圖檔案儲存於 `./result/` 目錄，檔案名稱基於 `<h2>` 元素提取的文字。
   - 控制台會顯示腳本執行進度及錯誤日誌。

## 專案結構
- **`main.py`**：主腳本，負責協調自動化流程。
- **`setup_driver.py`**：初始化 Selenium WebDriver，配置瀏覽器選項。
- **`login.py`**：處理登入流程，支援 TW FidO 手動認證。
- **`click_query.py`**：識別並點擊查詢按鈕，處理多頁查詢。
- **`extract_text.py`**：從 `<h2>` 元素提取文字，用於生成檔案名稱。
- **`capture_screenshot.py`**：截取並裁剪螢幕截圖，保存為 JPG。
- **`vote_stock.py`**：自動化投票流程，處理贊成、棄權等操作。
- **`config.py`**：載入 JSON 配置文件，實現參數化管理。
- **`config.json`**：儲存 URL、XPath 等配置資訊。

## 設計決策與技術亮點
作為一名資深的架構分析師，我在設計本專案時注重以下原則：

1. **模組化架構**：
   - 將功能拆分為獨立模組（如 `login.py`、`click_query.py`），降低耦合度，便於維護和功能擴展。
   - 每個模組負責單一職責，符合 SOLID 原則中的單一職責原則（SRP）。

2. **參數化配置**：
   - 使用 `config.json` 管理所有 URL 和 XPath，允許快速適應網站結構變更，無需修改程式碼。
   - 支援動態調整，如投票按鈕的 XPath 定義，增強腳本的靈活性。

3. **錯誤處理與穩定性**：
   - 在每個關鍵步驟（如登入、按鈕點擊、截圖）實現了異常處理，確保腳本在網路不穩定或頁面結構變更時的穩定性。
   - 使用 `WebDriverWait` 確保元素可見和可點擊，減少 Selenium 操作失敗的風險。

4. **可擴展性**：
   - 投票流程設計為可配置的按鈕序列（`button_steps`），允許輕鬆添加新的投票選項或調整流程。
   - 模組化設計支持未來新增功能，例如支援其他網站或自動化任務。

5. **Conda 環境支援**：
   - 專案適配 Conda 環境管理，確保依賴安裝的隔離性和一致性，適合跨平台開發和部署。

## 故障排除
- **Conda 環境問題**：確保已正確啟用 Conda 環境 (`conda activate stock_query`)，並檢查 Python 版本是否為 3.8 或以上。
- **ChromeDriver 錯誤**：確認 ChromeDriver 版本 134 已正確安裝，且路徑在 `setup_driver.py` 中正確配置。
- **登入失敗**：確保 TW FidO 認證在 60 秒內完成，且跳轉 URL 包含 `tc_estock_welshas`。
- **查詢按鈕未找到**：檢查網站結構是否變更，必要時更新 `click_query.py` 中的 XPath。
- **截圖問題**：裁剪座標可以自行調整 `(139, 326, 2407, 922)` 是否適用於當前螢幕解析度:`capture_screenshot.py` 。

## 許可證
本專案採用 MIT 許可證，詳情請參閱 `LICENSE` 文件（若適用）。
