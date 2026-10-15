from az.Page import Page
from selenium import webdriver
import time,unittest

class Case(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_01_login(self):
        po = Page(self.driver)
        po.luo_login()


if __name__ == '__main__':
    unittest.main()


