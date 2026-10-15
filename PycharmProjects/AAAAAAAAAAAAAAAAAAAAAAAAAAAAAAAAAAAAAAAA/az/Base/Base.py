from selenium.webdriver.support.ui import WebDriverWait

class Base():
    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        self.driver.get(url)

    def find_element(self,loc):
        try:
            WebDriverWait(self.driver,20,1).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            print(e)

    def click(self,loc):
        self.find_element(loc).click()

    def send_keys(self,loc,info):
        self.find_element(loc).send_keys(info)

    def text(self,loc):
        return self.find_element(loc).text


