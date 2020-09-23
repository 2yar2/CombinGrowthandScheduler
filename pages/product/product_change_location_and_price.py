from pages.locators.locators_change_location_and_price import LocationAndPrice
from pages.base_page import BasePage


class ChangeLocationAndPrice(BasePage):

    def cookies_close(self):
        to_cookies_close = self.browser.find_element(*LocationAndPrice.COOKIES_CLOSE)
        to_cookies_close.click()

    def current_location(self):
        self.browser.find_element(*LocationAndPrice.CURRENTLOCATION).click()
        self.browser.implicitly_wait(5)

#Europe
    def france(self):
        self.browser.find_element(*LocationAndPrice.FRANCE).click()

    def spain(self):
        self.browser.find_element(*LocationAndPrice.SPAIN).click()

    def price_in_euro_personal_card(self):
        euro = self.browser.find_element(*LocationAndPrice.PERSONALCARDSYMBOL).text
        assert euro == "€"

    def price_in_euro_business_card(self):
        euro = self.browser.find_element(*LocationAndPrice.BUSINESSCARDSYMBOL).text
        assert euro == "€"
#USA
    def united_states(self):
        self.browser.find_element(*LocationAndPrice.UNITEDSTATES).click()

    def price_in_dollar_personal_card(self):
        dollar = self.browser.find_element(*LocationAndPrice.PERSONALCARDSYMBOL).text
        assert dollar == "$"

    def price_in_dollar_business_card(self):
        dollar = self.browser.find_element(*LocationAndPrice.BUSINESSCARDSYMBOL).text
        assert dollar == "$"



