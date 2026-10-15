import HTMLTestRunner_cn
import logging
import yagmail

class Toolss():
    # 日志
    def log1(self):
        log = logging.basicConfig(level=logging.DEBUG,
                                  format='%(levelname)s - %(filename)s - %(message)s - %(asctime)s - %(lineno)d',
                                  filename='a3mall.log',
                                  filemode='a+')
        return log

    # 报告
    def bao(self):
        gao = HTMLTestRunner_cn.HTMLTestRunner(open('a3mall.html', 'wb'),
                                               title='a3mall测试',
                                               description='测试报告')
        return gao

    # 邮件
    def Email(self):
        email = yagmail.SMTP(user='wh15040504381@126.com',
                             password='DPqxrwyvPEn6CTqm',
                             host='smtp.126.com',
                             port='465')
        email.send(to='2760107445@qq.com',
                   subject='a3mall测试',
                   contents=['a3mall.html', 'a3mall.log'])

