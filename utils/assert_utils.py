"""通用响应断言工具类"""
class ResponseAssert:
    def __init__(self):
        # 初始化错误列表，存放所有校验失败信息
        self.err_list = []
    # HTTP 200校验，失败记录不中断
    def check_http_200(self,res):
        try:
            assert res.status_code == 200, f"HTTP状态码异常：预期200，实际{res.status_code}"
        except AssertionError as e:
            self.err_list.append(str(e))
    # 基础响应结构校验（message、status）
    def check_schema(self,resp_data):
        try:
            assert 'message' in resp_data, '响应缺少message字段'
            assert 'status' in resp_data, '响应缺少status字段'
        except AssertionError as e:
            self.err_list.append(str(e))
    # 业务成功状态码校验
    def check_business_success(self,resp_data,success_code="0000"):
        try:
            actual = resp_data.get("status")
            assert actual == success_code,f"业务状态码异常,预期{success_code},实际：{actual}"
        except AssertionError as e:
            self.err_list.append(str(e))
    # 业务失败状态码校验（反向用例）
    def check_business_fail(self,resp_data,fail_code="1001"):
        try:
            actual = resp_data.get("status")
            assert actual == fail_code, f"业务状态码异常,预期失败码{fail_code},实际：{actual}"
        except AssertionError as e:
            self.err_list.append(str(e))
    # 最后统一校验：如果存在错误，一次性抛全部失败信息
    def assert_all(self):
        if len(self.err_list) > 0:
            err_msg = "\n".join(self.err_list)
            assert False,f"【接口校验存在{len(self.err_list)}处错误]\n{err_msg}"
