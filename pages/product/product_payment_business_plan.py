from pages.locators.locators_payment_business_plan import PaymentPlan
from pages.base_page import BasePage
import time


class PaymentBusinessPlan(BasePage):

    def cookies_close(self):
        to_cookies_close = self.browser.find_element(*PaymentPlan.COOKIES_CLOSE)
        to_cookies_close.click()
        time.sleep(3)

    def button_business_subscribe_now(self):
        button = self.browser.find_element(*PaymentPlan.BUTTONBUSINESSSUBSCRIBENOW)
        button.click()

    def current_symbol_1(self):
        self.browser.find_element(*PaymentPlan.CURRENCYSYMBOL1)

    def price_value_1(self):
        self.browser.find_element(*PaymentPlan.PRICEVALUE1)

    def email(self):
        email = self.browser.find_element(*PaymentPlan.EMAIL)
        time.sleep(1)
        email.send_keys("openmedia2020@mail.ru")

    def first_and_last_name(self):
        name = self.browser.find_element(*PaymentPlan.FIRSTANDLASTNAME)
        time.sleep(1)
        name.send_keys("FOR TESTING")

    def country(self):
        self.browser.find_element(*PaymentPlan.COUNTRY).click()
        time.sleep(1)


    def united_states(self):
        us = self.browser.find_element(*PaymentPlan.UNITEDSTATES)
        time.sleep(1)
        us.click()

    def city(self):
        city = self.browser.find_element(*PaymentPlan.CITY)
        time.sleep(1)
        city.send_keys("Sacramento")

    def address(self):
        address = self.browser.find_element(*PaymentPlan.ADDRESS)
        time.sleep(1)
        address.send_keys("Solons Alley")

    def state(self):
        state = self.browser.find_element(*PaymentPlan.STATE)
        time.sleep(1)
        state.send_keys("California")

    def zip_code(self):
        zip = self.browser.find_element(*PaymentPlan.ZIPCODE)
        time.sleep(1)
        zip.send_keys("95811")

    def name_on_card(self):
        name = self.browser.find_element(*PaymentPlan.NAMEONCARD)
        name.send_keys("FOR TESTING")
        time.sleep(1)

    def card_number(self):
        number = self.browser.find_element(*PaymentPlan.CARDNUMBER).click()
        time.sleep(1)
        number.send_keys("4242424242424242")

    def expiration_date(self):
        date = self.browser.find_element(*PaymentPlan.EXPIRATIONDATE).click()
        date.send_keys("0125")

    def card_cvc(self):
        cvc = self.browser.find_element(*PaymentPlan.CARDCVC).click()
        time.sleep(30)
        cvc.send_keys("111")

    def current_symbol_2(self):
        self.browser.find_element(*PaymentPlan.CURRENCYSYMBOL2)

    def price_value_2(self):
        self.browser.find_element(*PaymentPlan.PRICEVALUE2)

    def subscribe(self):
        self.browser.find_element(*PaymentPlan.SUBSCRIBE).click()



#class PaymentPersonalPlan(BasePage):

#    def cookies_close(self):
#        to_cookies_close = self.browser.find_element(*PaymentPlan.COOKIES_CLOSE)
#        to_cookies_close.click()