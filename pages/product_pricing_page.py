from .locators_pricing import PricingLocators
from .base_page import BasePage
import time

class ProductPagePricing(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*PricingLocators.COOKIES_CLOSE)
        close.click()

    def plan_for_every_one(self):
        self.browser.find_element(*PricingLocators.PLANFOREVERYONE)

    def slider_growth(self):
        self.browser.find_element(*PricingLocators.SLIDERGROWTH)
# карточка бесплатного плана
    def starter_plan(self):
        self.browser.find_element(*PricingLocators.STARTER)

    def starter_heading(self):
        self.browser.find_element(*PricingLocators.STARTERHEADING)

    def starter_get_starter(self):
        self.browser.find_element(*PricingLocators.STARTERGETSTARTED)

    def starter_features(self):
        self.browser.find_element(*PricingLocators.STARTERCARDFEATURES)

#карточка персонального плана
    def personal(self):
        self.browser.find_element(*PricingLocators.PERSONAL)

    def personal_heading(self):
        self.browser.find_element(*PricingLocators.STARTERHEADING)

    def personal_price(self):
        self.browser.find_element(*PricingLocators.PERSONALPRICE)

    def personal_symbol(self):
        self.browser.find_element(*PricingLocators.PERSONALSYMBOL)

    def personal_subscribe(self):
        self.browser.find_element(*PricingLocators.PERSONALSUBSCRIBENOW)

    def personal_features(self):
        self.browser.find_element(*PricingLocators.PERSONALCARDFEATURES)

# карточка бизнес плана
    def business_plan(self):
        self.browser.find_element(*PricingLocators.BUSINESS)

    def business_heading(self):
        self.browser.find_element(*PricingLocators.BUSINESSHEADING)

    def business_price(self):
        self.browser.find_element(*PricingLocators.BUSINESSPRICE)

    def business_symbol(self):
        self.browser.find_element(*PricingLocators.BUSINESSSYMBOL)

    def business_subscribe(self):
        self.browser.find_element(*PricingLocators.BUSINESSSUBSCRIBENOW)

    def business_feature(self):
        self.browser.find_element(*PricingLocators.BUSINESSCARDFEATURES)

# location
    def current_location(self):
        self.browser.find_element(*PricingLocators.CURRENTLOCATION)

    def asked_question(self):
        self.browser.find_element(*PricingLocators.ASKEDQUESTIONS)

# Часто задаваемые вопросы
    def cancel_subscribe(self):
        dropdown = self.browser.find_element(*PricingLocators.HOWCANCANCELSUB)
        dropdown.click()

    def cancel_subscribe_answer(self):
        self.browser.find_element(*PricingLocators.HOWCANCANCELSUBANSWER)

    def cancel_subscribe_list(self):
        self.browser.find_element(*PricingLocators.HOWCANCANCELTLIST)

    def cancel_subscribe_link(self):
        self.browser.find_element(*PricingLocators.HOWCANCANCELTLINK)

    def personal_to_business(self):
        dropdown = self.browser.find_element(*PricingLocators.PERSONALTOBUSINESS)
        dropdown.click()

    def personal_to_business_answer(self):
        self.browser.find_element(*PricingLocators.PERSONALTOBUSINESSANSWER)

    def personal_to_business_list(self):
        self.browser.find_element(*PricingLocators.PERSONALTOBUSINESSLIST)

    def personal_to_business_link(self):
        self.browser.find_element(*PricingLocators.PERSONALTOBUSINESSLINK)

    def business_to_personal(self):
        dropdown = self.browser.find_element(*PricingLocators.BUSINESSTOPERSONAL)
        dropdown.click()

    def business_to_personal_answer(self):
        self.browser.find_element(*PricingLocators.BUSINESSTOPERSONALANSWER)

    def business_to_personal_link_cancel(self):
        self.browser.find_element(*PricingLocators.BUSINESSTOPERSONALLINKCANCEL)

    def business_to_personal_link_sub(self):
        self.browser.find_element(*PricingLocators.BUSINESSTOPERSONALLINKSUB)

    def receive_the_key(self):
        dropdown = self.browser.find_element(*PricingLocators.RECEIVETHEKEY)
        dropdown.click()

    def receive_the_key_answer(self):
        self.browser.find_element(*PricingLocators.RECEIVETHEKEYANSWER)

    def receive_the_key_list(self):
        self.browser.find_element(*PricingLocators.RECEIVETHEKEYLIST)

    def receive_the_key_link(self):
        self.browser.find_element(*PricingLocators.RECEIVETHEKEYLINK)

    def can_us_license(self):
        dropdown = self.browser.find_element(*PricingLocators.CANIUSEONELICENSE)
        dropdown.click()

    def can_us_license_answer(self):
        self.browser.find_element(*PricingLocators.CANIUSEONELICENSEANSWER)

    def refund_policy(self):
        dropdown = self.browser.find_element(*PricingLocators.REFUNDPOLICY)
        dropdown.click()

    def refund_policy_answer(self):
        self.browser.find_element(*PricingLocators.REFUNDPOLICYANSWER)

    def refund_policy_link(self):
        self.browser.find_element(*PricingLocators.REFUNDPOLICYLINK)

    def sub_payment(self):
        dropdown = self.browser.find_element(*PricingLocators.SUBPAYMENT)
        dropdown.click()

    def sub_payment_answer(self):
        self.browser.find_element(*PricingLocators.SUBPAYMENTANSWER)

    def sub_payment_link(self):
        self.browser.find_element(*PricingLocators.SUBPAYMENTLINK)

    def starter_plan_free(self):
        dropdown = self.browser.find_element(*PricingLocators.STARTERPLANFREE)
        dropdown.click()

    def starter_plan_free_answer(self):
        dropdown = self.browser.find_element(*PricingLocators.STARTERPLANFREEANSWER)
        dropdown.click()

    def update_billing(self):
        dropdown = self.browser.find_element(*PricingLocators.UPDATEBILLING)
        dropdown.click()

    def update_billing_answer(self):
        self.browser.find_element(*PricingLocators.UPDATEBILLINGANSWER)

    def update_billing_link(self):
        self.browser.find_element(*PricingLocators.UPDATEBILLINGLINK)
# мы в соц сетях
    def contact_us(self):
        self.browser.find_element(*PricingLocators.CONTACTUS)

    def contact_us_text(self):
        self.browser.find_element(*PricingLocators.CONTACTUSTEXT)

    def combin_blog(self):
        self.browser.find_element(*PricingLocators.COMBINBLOG)

    def combin_twitter(self):
        self.browser.find_element(*PricingLocators.COMBINTWITTER)

    def combin_youtube(self):
        self.browser.find_element(*PricingLocators.COMBINYOUTUBE)

    def combin_reddit(self):
        self.browser.find_element(*PricingLocators.COMBINREDDIT)

# связь с нами
    def support_team(self):
        self.browser.find_element(*PricingLocators.SUPPORTTEAM)

    def support_team_email(self):
        self.browser.find_element(*PricingLocators.SUPPORTTEAMEMAIL)

    def marketing_team(self):
        self.browser.find_element(*PricingLocators.MARKETINGTEAM)

    def marketing_team_email(self):
        self.browser.find_element(*PricingLocators.MARKETINGTEAMEMAIL)

    def dev_team(self):
        self.browser.find_element(*PricingLocators.DEVELOPMENTTEAM)

    def dev_team_email(self):
        self.browser.find_element(*PricingLocators.DEVELOPMENTTEAMEMAIL)

class PricingScheduler(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*PricingLocators.COOKIES_CLOSE)
        close.click()

    def slider_scheduler(self):
        slider = self.browser.find_element(*PricingLocators.SLIDERSCHEDULER)
        slider.click()

    def starter_scheduler(self):
        self.browser.find_element(*PricingLocators.STARTERSCHEDULER)

    def personal_scheduler(self):
        self.browser.find_element(*PricingLocators.PERSONALSCHEDULER)

    def business_scheduler(self):
        self.browser.find_element(*PricingLocators.BUSINESSSCHEDULER)

    def slider_growth(self):
        slider = self.browser.find_element(*PricingLocators.SLIDERGROWTH)
        slider.click()
        time.sleep(1)
