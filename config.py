import json
# 讀取參數檔
def load_config(config_path="config.json"):
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"錯誤：找不到 {config_path} 檔案")
        raise
    except json.JSONDecodeError:
        print(f"錯誤：{config_path} 格式錯誤")
        raise