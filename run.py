import pytest,os
from utils.tools import Tools
if __name__ == '__main__':
    Tools().log()
    pytest.main()
    os.system('allure generate ./report/allure-results -o ./report/allure-report --clean')
    Tools().Email()