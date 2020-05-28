from pages.base_page import BasePage
from pages.locators.locators_aboutus import AboutUsPageLocators
import time


class ProductPageAboutUs(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*AboutUsPageLocators.COOKIES_CLOSE)
        close.click()


    def about_us_headline(self):
        self.browser.find_element(*AboutUsPageLocators.ABOUTUSHEADLINE)

    def about_us_text(self):
        self.browser.find_element(*AboutUsPageLocators.ABOUTUSTEXT)


    def contact_us_heading(self):
        self.browser.find_element(*AboutUsPageLocators.CONTACTUSHEADLINE)

    def contact_us_text(self):
        self.browser.find_element(*AboutUsPageLocators.CONTACTUSTEXT)

#Блоги
    def combin_blog(self):
        self.browser.find_element(*AboutUsPageLocators.COMBINBLOG)

    def combin_twitter(self):
        self.browser.find_element(*AboutUsPageLocators.COMBINTWITTER)

    def combin_youtube(self):
        self.browser.find_element(*AboutUsPageLocators.COMBINYOUTUBE)

    def combin_reddit(self):
        self.browser.find_element(*AboutUsPageLocators.COMBINREDDIT)

# Связь с нами
    def support_team(self):
        self.browser.find_element(*AboutUsPageLocators.SUPPORTTEAM)

    def support_team_email(self):
        self.browser.find_element(*AboutUsPageLocators.SUPPORTTEAMEMAIL)

    def marketing_team(self):
        self.browser.find_element(*AboutUsPageLocators.MARKETINGTEAM)

    def marketing_team_email(self):
        self.browser.find_element(*AboutUsPageLocators.MARKETINGTEAMEMAIL)

    def dev_team(self):
        self.browser.find_element(*AboutUsPageLocators.DEVELOPMENTTEAM)

    def dev_team_email(self):
        self.browser.find_element(*AboutUsPageLocators.DEVELOPMENTTEAMEMAIL)

#Адрес оффисофф
    def euro_office(self):
        self.browser.find_element(*AboutUsPageLocators.EUROPEANOFFICE)

    def euro_office_heading(self):
        self.browser.find_element(*AboutUsPageLocators.EUROPEANADDRESSHEADING)

    def euro_office_text(self):
        self.browser.find_element(*AboutUsPageLocators.EUROPEANADDRESSTEXT)

    def rus_office(self):
        self.browser.find_element(*AboutUsPageLocators.RUSSIANOFFICE)

    def rus_office_heading(self):
        self.browser.find_element(*AboutUsPageLocators.RUSSIANOFFICEADDRESSHEADING)

    def rus_office_text(self):
        self.browser.find_element(*AboutUsPageLocators.RUSSIANOFFICEADDRESSTEXT)

# БЛОК ЗАГРУЗКИ

    def downloadblock_logo(self):
        self.browser.find_element(*AboutUsPageLocators.DOWNLOADBLOCKLOGO)

    def downloadblock_text(self):
        self.browser.find_element(*AboutUsPageLocators.DOWNLOADBLOCKTEXT)

    def downloadblock_email(self):
        email = self.browser.find_element(*AboutUsPageLocators.DOWNLOADBLOCKINPUTEMAIL)
        email.send_keys("openmedia2020@mail.ru")

    def download_checkbox(self):
        checkbox = self.browser.find_element(*AboutUsPageLocators.DOWNLOADBLOCKCHECKBOX)
        checkbox.click()

    def download_checbox_text(self):
        self.browser.find_element(*AboutUsPageLocators.DOWNLOADBLOCKCHECKBOXTEXT)

    def download_try_free(self):
        try_free = self.browser.find_element(*AboutUsPageLocators.DOWNLOADBLOCKTRYFREE)
        try_free.click()
        time.sleep(3)

    def assept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()
        time.sleep(1)

    def opacity(self):
        self.browser.find_element(*AboutUsPageLocators.DOWNLOADBLOCKOPACITY)

    def privacy_policy(self):
        self.browser.find_element(*AboutUsPageLocators.DOWNLOADBLOCKPRIVACYPOLICY)

    def os(self):
        self.browser.find_element(*AboutUsPageLocators.DOWNLOADBLOCKOS)

    def avialable(self):
        self.browser.find_element(*AboutUsPageLocators.DOWNLOADBLOCKAVALIABLE)
