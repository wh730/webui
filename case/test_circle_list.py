import allure
import pytest
import requests.exceptions
from utils.assert_utils import ResponseAssert
from conftest import api
import logging
class TestDims():
    @allure.feature('圈子列表')
    @allure.title('查询圈子列表成功')
    def test_circle(self,api):
        with allure.step('请求参数'):
            url = '/small/circle/v1/findCircleList?page=1&count=5'
            headers = {"Content-Type": "application/json"}
        with allure.step('发送请求'):
            try:
                res = api.get(url,headers=headers)
                logging.info(res.text)
            except requests.exceptions.RequestException as e:
                pytest.fail(f"请求失败:{e}")
        # 实例化校验对象
        asserter = ResponseAssert()
        # 状态码 + 响应结构 + 核心业务字段 + 必要DB校验
        asserter.check_http_200(res)
        # 响应结构断言
        resp_data = res.json()
        asserter.check_schema(resp_data)
        # 核心业务字段断言
        asserter.check_business_success(resp_data,success_code='0000')