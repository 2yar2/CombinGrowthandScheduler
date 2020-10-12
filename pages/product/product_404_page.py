from pages.base_page import BasePage
from pages.locators.locators_404 import Locators404



class Product404Page(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*Locators404.COOKIES_CLOSE)
        close.click()

    def page_not_found(self):
        self.browser.find_element(*Locators404.PAGENOTFOUND)

    def error_text(self):
        self.browser.find_element(*Locators404.ERRORPAGETEXT)

    def error_link(self):
        href = self.browser.find_element(*Locators404.ERRORPAGELINK).get_attribute("href")
        assert href == 'https://www.combin.com/'
