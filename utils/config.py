import requests
# 只导入环境读取工具，不再写读取文件代码
from utils.env_loader import ENV_URL, REQ_TIMEOUT

# 你原来的Config类【一行代码都不用删减】
class Config:
    def __init__(self, url):
        self.url = url
        self.session = requests.session()

    def request(self, method, path, **kwargs):
        url = f'{self.url}{path}'
        kwargs.setdefault("timeout", REQ_TIMEOUT)
        resp = self.session.request(method, url,** kwargs)
        return resp

    def post(self, path, **kwargs):
        return self.request(method='POST', path=path, **kwargs)

    def get(self, path,** kwargs):
        return self.request(method='GET', path=path, **kwargs)

    def put(self, path,** kwargs):
        return self.request(method='PUT', path=path, **kwargs)

    def delete(self, path,** kwargs):
        return self.request(method='DELETE', path=path, **kwargs)

    def close(self):
        self.session.close()

# 全局实例，自动带入当前环境地址，fixture不用硬写url
api_client = Config(ENV_URL)