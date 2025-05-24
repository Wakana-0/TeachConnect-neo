import os
import json
from loguru import logger

# 设置存储路径
APP_DATA_PATH = os.path.join(os.getenv("APPDATA"), "TeachConnect_Data")
OLD_APP_DATA_PATH = os.path.join(os.getenv("APPDATA"), "TConect")

USER_DATA_PATH = os.path.join(APP_DATA_PATH, "User")
OLD_USER_DATA_PATH = os.path.join(OLD_APP_DATA_PATH, "User")

LOG_PATH = os.path.join(APP_DATA_PATH, "log")

CACHE_PATH = os.path.join(APP_DATA_PATH, "cache")

IP_STORAGE_FILE = os.path.join(CACHE_PATH, "IPs.json")

NAME_STORAGE_FILE = os.path.join(CACHE_PATH, "Names.json")

USER_CREDENTIALS_FILE = os.path.join(USER_DATA_PATH, "UserInfo.json")
OLD_USER_CREDENTIALS_FILE = os.path.join(OLD_USER_DATA_PATH, "UserInfo.json")

def load_recent_data(filepath):
    logger.debug(f"加载文件: {filepath}")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.debug(f"加载成功: {data}")
            return data
    logger.debug("文件不存在，返回空字典")
    return {}



def save_recent_data(filepath, data):
    logger.debug(f"保存数据到 {filepath}，数据: {data}")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    # 测试
    print(load_recent_data(OLD_USER_CREDENTIALS_FILE))