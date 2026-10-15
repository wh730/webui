import time

from selenium.webdriver.common.by import By
from az.Base import Base

class Page(Base):
    login_loc = (By.XPATH,'/html/body/div[1]/div/div[2]/ul/li[1]/a')
    def login(self):
        self.click(self.login_loc)

    dy_loc = (By.CLASS_NAME,'reg-new')
    def dy(self):
        return self.text(self.dy_loc)

    yhm_loc = (By.NAME,'username')
    def yhm(self):
        self.send_keys(self.yhm_loc,'13811033962')

    mima_loc = (By.XPATH,'/html/body/div[4]/div/div[1]/div[2]/form/div[2]/span[2]/input')
    def mima(self):
        self.send_keys(self.mima_loc,'123456')

    deng_loc = (By.XPATH,'/html/body/div[4]/div/div[1]/div[2]/form/div[5]/a')
    def deng(self):
        self.click(self.deng_loc)

    def luo_login(self):
        self.open_url('http://10.59.9.12:7001/')
        time.sleep(2)
        self.login()
        print(self.dy())
        self.yhm()
        self.mima()
        time.sleep(10)
        self.deng()


