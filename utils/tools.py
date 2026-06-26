import os.path
import logging
import yagmail
# 从独立env_loader拿配置
from utils.env_loader import MAIL, LOG_PATH

class Tools:
    def log(self):
        log = logging.basicConfig(
            level=logging.INFO,
            format='%(levelname)s %(filename)s %(message)s %(asctime)s %(lineno)d',
            filename=LOG_PATH,
            filemode='a+'
        )
        return log

    def Email(self):
        mail_user = MAIL["user"]
        mail_pwd = MAIL["pwd"]
        mail_host = MAIL["host"]
        mail_port = MAIL["port"]
        mail_to = MAIL["to"]
        mail = yagmail.SMTP(user=mail_user, password=mail_pwd, host=mail_host, port=mail_port)
        log_path = os.path.abspath(LOG_PATH)
        mail.send(to=mail_to, subject='维度电商测试报告', contents='本次自动化测试用例执行完毕，详情见附件日志文件', attachments=log_path)
        mail.close()