from pages.locators.locators_intercom import LocatorsIntercom
from pages.base_page import BasePage
import time


class ProductIntercom(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*LocatorsIntercom.COOKIES_CLOSE)
        close.click()
        time.sleep(1)

    def intercom_launcher(self):
        self.browser.find_element(*LocatorsIntercom.INTERCOMLAUNCHER).click()
        time.sleep(1)

    def send_us_a_message(self):
        message = self.browser.find_element(*LocatorsIntercom.SENDUSAMESSAGE)
        message.click()
        time.sleep(2)

    def input_email(self):
        email = self.browser.find_element(*LocatorsIntercom.INPUTEMAIL).click()
        email.send_keys("openmedia2020@mail.ru")

    def write_your_message(self):
        message = self.browser.find_element(*LocatorsIntercom.WRITEYOURMESSAGE)
        message.send_keys("НЕ ОБРАЩАТЬ ВНИМАНИЕ! AUTOMATION TEST!")

    def send_message(self):
        self.browser.find_element(*LocatorsIntercom.SENDMESSAGE).click()

    def replies_answer(self):
        self.browser.find_element(*LocatorsIntercom.REPLIESEANSWER)

    def email_answer(self):
        self.browser.find_element(*LocatorsIntercom.EMAILANSWER)

    def more_details(self):
        self.browser.find_element(*LocatorsIntercom.MOREDETAILSANSWER)

    def name_answer(self):
        self.browser.find_element(*LocatorsIntercom.NAMEANSWER)

    def input_name(self):
        self.browser.find_element(*LocatorsIntercom.INPUTNAME).send_keys("OPEN MEDIA NN")

    def submeet(self):
        self.browser.find_element(*LocatorsIntercom.SUBMEET).click()
        time.sleep(2)

    def thank_answer(self):
        self.browser.find_element(*LocatorsIntercom.THANKSANSWER)