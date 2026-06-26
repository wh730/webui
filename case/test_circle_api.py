import os.path
import allure
import pytest
import requests.exceptions
from utils.assert_utils import ResponseAssert
from conftest import api,token
import logging
class TestDims():
    @allure.feature('圈子列表')
    @allure.title('查询圈子列表成功')
    @pytest.mark.circle
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

    @allure.feature('发布我的圈子')
    @allure.title('圈子发布成功')
    def test_pub(self,api, token):
        uid,sid = token  # 解包元祖
        with allure.step('请求参数'):
            url = '/small/circle/verify/v1/releaseCircle'
            headers = {"userid": str(uid),'sessionid':sid}
            data = {"commodityId":"1","content":"运动鞋"}
            img_path = r'C:\Users\PY\PycharmProjects\dimension-mall-api\png\aef57696006b60c817db222d1d801d8c.png'
            files = {"img":(os.path.basename(img_path),open(img_path,'rb'),'image/png')}
        with allure.step('发送请求'):
            try:
                res = api.post(url, headers=headers,data=data,files=files)
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
        asserter.check_business_success(resp_data, success_code='0000')

    @allure.feature('我的圈子')
    @allure.title('我的圈子查看成功')
    def test_my_circle(self, api, token):
        uid, sid = token  # 解包元祖
        with allure.step('请求参数'):
            url = '/small/circle/verify/v1/releaseCircle?page=1&count=5'
            headers = {"userid": str(uid), 'sessionid': sid}
        with allure.step('发送请求'):
            try:
                res = api.get(url, headers=headers)
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
        asserter.check_business_success(resp_data, success_code='0000')

    @allure.feature('删除我发布的圈子')
    @allure.title('成功删除我发布的圈子')
    def test_my_circle(self, api, token,circle):
        uid, sid = token  # 解包元祖
        cid = circle
        with allure.step('请求参数'):
            url = f'/small/circle/verify/v1/deleteCircle?circleId={cid}'
            headers = {"userid": str(uid), 'sessionid': sid}
        with allure.step('发送请求'):
            try:
                res = api.delete(url, headers=headers)
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
        asserter.check_business_success(resp_data, success_code='0000')






