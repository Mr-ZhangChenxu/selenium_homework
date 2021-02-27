from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    base_url = ''

    def __init__(self, driver: WebDriver = None):
        # 如果浏览器为None，初始化浏览器
        if driver == None:
            # 复用浏览器
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.implicitly_wait(5)
        # 如果浏览器不为 None 传入driver
        else:
            self.driver = driver

        if self.base_url != '':
            self.driver.get(self.base_url)

    # 定义find_element方法
    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    # 定义find_elements方法
    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    # 定义显示等待，等待元素可点击
    def wait_for_click(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
