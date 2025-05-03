from PIL import Image
import io
import os  # 加入 os 模組

def capture_screenshot(driver, filename, folderName):
    # 步驟 4：擷取當前視窗截圖
    print("開始擷取當前視窗截圖...")
    # 設置窗口大小（可根據需要調整）
    driver.set_window_size(1920, 1080)  # 設置為常見解析度，確保包含目標範圍

    # 直接擷取當前視窗截圖
    screenshot = driver.get_screenshot_as_png()
    full_image = Image.open(io.BytesIO(screenshot))

    # 裁剪指定範圍 (x:139~2407, y:326~922)
    crop_box = (139, 326, 2407, 922)  # (left, upper, right, lower)
    cropped_image = full_image.crop(crop_box)

    # 檢查並建立資料夾
    output_dir = f"./result/{folderName}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"已建立資料夾：{output_dir}")

    # 保存為 JPG
    output_path = f"{output_dir}/{filename}.jpg"
    cropped_image.save(output_path, "JPEG", quality=85)
    print(f"截圖已保存為：{output_path}")