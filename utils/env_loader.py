import os
import yaml
from dotenv import load_dotenv

# 1. 获取项目根目录（dimension-mall-api 文件夹）
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 拼接完整文件路径
env_file_path = os.path.join(ROOT_PATH, ".env")
yaml_file_path = os.path.join(ROOT_PATH, ".env.yaml")

# 加载.env
load_dotenv(dotenv_path=env_file_path)
CURR_ENV = os.getenv("APP_ENV", "test")

# 加载.env.yaml
with open(yaml_file_path, "r", encoding="utf-8") as f:
    YAML_CFG = yaml.safe_load(f)

# 匹配环境域名
if CURR_ENV == "dev":
    BASE_URL = os.getenv("DEV_BASE_URL")
elif CURR_ENV == "prod":
    BASE_URL = os.getenv("PROD_BASE_URL")
else:
    BASE_URL = os.getenv("TEST_BASE_URL")

# 导出常量
MAIL = YAML_CFG["mail"]
LOG_PATH = YAML_CFG["log_path"]
REQ_TIMEOUT = YAML_CFG["timeout"]
ENV_URL = BASE_URL
ENV_NAME = CURR_ENV