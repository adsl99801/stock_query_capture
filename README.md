# Stock Query Capture Script

stock_query_capture

This project is a Python-based automation script designed to interact with the TDCC (Taiwan Depository & Clearing Corporation) stock services website. It automates the process of logging in, navigating through query buttons, extracting text from specific elements, and capturing screenshots of designated page areas. The script uses Selenium WebDriver for browser automation and includes modular components for different functionalities.

## Features
- **Automated Login**: Opens the TDCC login page and waits for manual authentication via TW FidO.
- **Query Button Processing**: Identifies and clicks query buttons for different stock information pages.
- **Text Extraction**: Extracts text from the first `<h2>` element on the page to generate meaningful filenames.
- **Screenshot Capture**: Captures and crops screenshots of specific page areas, saving them as JPG files.
- **Configurable**: Uses a JSON configuration file to manage URLs and other settings.

## Prerequisites
- **Python 3.8+**
- **Chrome Browser** (compatible with ChromeDriver version 134)
- **ChromeDriver** (version 134, placed at `D:\Users\keith\project\driver\chromedriver.exe`)
- **Required Python Packages**:
  ```bash
  pip install selenium pillow
  ```

## Installation
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   If a `requirements.txt` file is not present, manually install the required packages:
   ```bash
   pip install selenium pillow
   ```

3. **Set Up ChromeDriver**:
   - Download ChromeDriver version 134 from the [official site](https://chromedriver.chromium.org/downloads).
   - Place the `chromedriver.exe` file at `D:\Users\keith\project\driver\chromedriver.exe`. Update the path in `setup_driver.py` if necessary.

4. **Prepare Configuration**:
   - Ensure the `config.json` file is present in the project root with the correct URLs:
     ```json
     {
         "login_url": "https://stockservices.tdcc.com.tw/evote/login/goTwFidO.html",
         "query_buttons_url": "https://stockservices.tdcc.com.tw/evote/shareholder/000/tc_estock_welshas.html?stockInfo=",
         "redirect_url_contains": "tc_estock_welshas"
     }
     ```

## Usage
1. **Run the Script**:
   ```bash
   python main.py
   ```
2. **Follow Prompts**:
   - The script will open a Chrome browser and navigate to the TDCC login page.
   - Complete the TW FidO authentication manually in the browser.
   - After successful login and redirection, press **Enter** in the terminal to continue.
3. **Output**:
   - Screenshots are saved in the `./result/<stock_info_page>/` directory, named based on extracted `<h2>` text or a UUID if extraction fails.
   - Console logs provide details on the script’s progress and any errors.

## Project Structure
- **`main.py`**: Main script that orchestrates the automation workflow.
- **`setup_driver.py`**: Configures and initializes the Selenium WebDriver.
- **`login.py`**: Handles the login process with manual TW FidO authentication.
- **`click_query.py`**: Manages the identification and clicking of query buttons.
- **`extract_text.py`**: Extracts text from `<h2>` elements for naming screenshots.
- **`capture_screenshot.py`**: Captures and crops screenshots, saving them as JPGs.
- **`config.py`**: Loads configuration from `config.json`.
- **`config.json`**: Stores URLs and settings for the script.

## Notes
- **ChromeDriver Path**: Ensure the ChromeDriver path in `setup_driver.py` matches your setup.
- **Manual Login**: The script requires manual TW FidO authentication due to security restrictions.
- **Error Handling**: The script includes basic error handling but may require adjustments for specific edge cases.
- **Screenshot Cropping**: The cropping coordinates `(139, 326, 2407, 922)` are hardcoded in `capture_screenshot.py`. Adjust as needed for different screen resolutions or content layouts.

## Troubleshooting
- **ChromeDriver Error**: Verify that ChromeDriver version 134 is correctly installed and the path in `setup_driver.py` is accurate.
- **Login Failure**: Ensure the TW FidO authentication is completed within 60 seconds, and the redirect URL contains `tc_estock_welshas`.
- **No Query Buttons Found**: Check the website’s structure and update the XPath in `click_query.py` if the button class or text changes.
- **Screenshot Issues**: Verify the cropping coordinates and ensure the browser window size is set appropriately.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details (if applicable).