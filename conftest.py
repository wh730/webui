import pytest
# 替换原有导入，使用全局实例
from utils.config import api_client
# 导入数据初始化/清理工具
from utils.data_clean import DataPrepareClean

# ===================== 新增全局前置后置（session级别，整套用例只执行一次） =====================
@pytest.fixture(scope="session", autouse=True)
def before_all_case():
    # 整套用例执行前，执行数据初始化
    DataPrepareClean.init_test_data()
    yield
    # 整套用例全部跑完，执行数据清理
    DataPrepareClean.clear_test_data()

# ===================== 你原来的3个fixture【代码完全不变，仅修改api实例】 =====================
@pytest.fixture(scope='session')
def api():
    # 不再硬写url，直接使用全局环境实例
    yield api_client
    api_client.close()

# 提取登录凭证（原有代码一字不动）
@pytest.fixture(scope='session')
def token(api):
    url = '/small/user/v1/login'
    headers = {"Content-Type": "application/json"}
    body = {"phone": "15807934407", "pwd": "123456Aa"}
    res = api.post(url, headers=headers, json=body)
    uid = res.json()['result']['userId']
    sid = res.json()['result']['sessionId']
    return uid, sid

# 提取圈子ID（原有代码一字不动）
@pytest.fixture(scope='session')
def circle(api, token):
    uid, sid = token  # 解包元组
    url = '/small/circle/verify/v1/findMyCircleById?page=1&count=5'
    headers = {"userId": str(uid), "sessionId": sid}
    res = api.get(url, headers=headers)
    cid = res.json()['result'][0]['id']
    return cid