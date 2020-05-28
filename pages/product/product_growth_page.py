from pages.locators.locators_growth import MainPageLocators
from pages.locators.locators_growth import DownloadBlockLocators
from pages.base_page import BasePage
import time


class ProductPage(BasePage):

    def cookies_close(self):
        to_cookies_close = self.browser.find_element(*MainPageLocators.COOKIES_CLOSE)
        to_cookies_close.click()

    def click_to_growth(self):
        to_growth = self.browser.find_element(*MainPageLocators.GROWTH)
        assert self.is_element_present(
            *MainPageLocators.GROWTH), "View daily, weekly and monthly account activity statistics in-app. Track the followers count, see how many accounts followed and unfollowed you. Monitor the number of received likes and comments."
        to_growth.click()

    def click_to_advanced(self):
        to_advanced = self.browser.find_element(*MainPageLocators.ADVANCED)
        assert self.is_element_present(
            *MainPageLocators.ADVANCED), "Find interesting profiles and publications by using and combining different search queries. Run searches by hashtag, location, specific account’s following, followers, likers and commenters, and by bio."
        to_advanced.click()

    def click_to_gender(self):
        to_gender = self.browser.find_element(*MainPageLocators.GENDER)
        assert self.is_element_present(
            *MainPageLocators.GENDER), "Specify the following and followers quantity, select male or female gender, and pick from a variety of languages the preferred ones. Define the target audience with precision using the demographic filters"
        to_gender.click()

    def click_to_machine(self):
        to_machine = self.browser.find_element(*MainPageLocators.MACHINE)
        assert self.is_element_present(
            *MainPageLocators.MACHINE), "Identify low quality accounts with the help of the breakthrough technology. Eliminate pointless engagement and save the limited quantity of daily available actions for following, liking and commenting, to spend it on real, genuinely interested Instagram users"
        to_machine.click()

    def click_to_audience(self):
        to_audience = self.browser.find_element(*MainPageLocators.AUDIENCE)
        assert self.is_element_present(
            *MainPageLocators.AUDIENCE), "Detect who doesn’t follow you back and unfollow them in convenient batches. Track the accounts you unfollowed and automatically prevent following them or interacting ever again. Protect important accounts from accidental unfollowing. Filter and export your user lists to Excel"
        to_audience.click()

    def click_to_repetitive(self):
        to_repetitive = self.browser.find_element(*MainPageLocators.REPETITIVE)
        assert self.is_element_present(
            *MainPageLocators.REPETITIVE), "Engage multiple Instagram accounts and posts at once instead of manually interacting with the content of each separate user. Bulk-follow, unfollow, like and comment. Create comment templates for different topics and purposes, and leave them in batch"
        to_repetitive.click()

    def click_to_multiple(self):
        to_multiple = self.browser.find_element(*MainPageLocators.MULTIPLE)
        assert self.is_element_present(
            *MainPageLocators.MULTIPLE), "Engage multiple Instagram accounts and posts at once instead of manually interacting with the content of each separate user. Bulk-follow, unfollow, like and comment. Create comment templates for different topics and purposes, and leave them in batch"
        to_multiple.click()

    def img_performance_statistics(self):
        self.browser.find_element(*MainPageLocators.IMGPERFORMANCESTATISTICS)

    def img_detect(self):
        self.browser.find_element(*MainPageLocators.IMGDETECT)

    def text_feature_heading(self):
        self.browser.find_elements(*MainPageLocators.TEXTFEATUREHEADING)

    def text_feature_list(self):
        self.browser.find_elements(*MainPageLocators.TEXTINFOFEATURELIST)

    def img_check_quality(self):
        self.browser.find_element(*MainPageLocators.IMGCHECKQUALITY)

    def img_find_target(self):
        self.browser.find_element(*MainPageLocators.IMGFINDTARGET)

    def img_instagram_influencers(self):
        self.browser.find_element(*MainPageLocators.IMGINFLUENCERS)

    def img_manage_activity(self):
        self.browser.find_element(*MainPageLocators.IMGMANAGEACTIVITY)

    def img_scheduler_promo(self):
        self.browser.find_element(*MainPageLocators.IMGSCHEDULERPROMO)

    def other_logo_scheduler(self):
        self.browser.find_element(*MainPageLocators.OTHERLOGOPROMOSCHEDULER)

    def users_feedback(self):
        self.browser.find_elements(*MainPageLocators.USERSFEEDBACK)

    def users_name_feedback(self):
        self.browser.find_elements(*MainPageLocators.USERSNAMEFEEDBACK)

    #def arrow_button_right(self):
    #    button_right = self.browser.find_element(*MainPageLocators.ARROWBUTTONRIGHT)
    #    button_right.click()

    #def arrow_button_left(self):
    #    button_left = self.browser.find_elements(*MainPageLocators.ARROWBUTTONLEFT)
    #    button_left.click()

    def users_trust_us(self):
        self.browser.find_element(*MainPageLocators.USERSTRUSTUS)

    def logo_numeriques(self):
        self.browser.find_element(*MainPageLocators.NUMERIQUES)

    def logo_sej(self):
        self.browser.find_element(*MainPageLocators.SEJ)

    def logo_forbes(self):
        self.browser.find_element(*MainPageLocators.FORBES)

    def logo_online_marketing(self):
        self.browser.find_element(*MainPageLocators.ONLINEMARKETING)

    def logo_product_hunt(self):
        self.browser.find_element(*MainPageLocators.PRODUCTHUNT)

    def link_read_all_publication(self):
        self.browser.find_element(*MainPageLocators.LINKREADALLPUBLICATION)

    def link_learn_more(self):
        self.browser.find_elements(*MainPageLocators.LINKLEARNMORE)

    def link_news_learn_more(self):
        self.browser.find_element(*MainPageLocators.LINKNEWSLEARNMORE)

class ProductPromo(BasePage):

    def cookies_close(self):
        to_cookies_close = self.browser.find_element(*MainPageLocators.COOKIES_CLOSE)
        to_cookies_close.click()

    def email_for_start(self):
        email_start = self.browser.find_element(*DownloadBlockLocators.EMAILFORSTART)
        email_start.send_keys("openmedia@mail.ru")

    def button_try_free(self):
        try_free = self.browser.find_element(*DownloadBlockLocators.BUTTONTRYFREE)
        try_free.click()
        time.sleep(3)


    def button_try_for_free_promo(self):
        try_free_promo = self.browser.find_element(*DownloadBlockLocators.BUTTONTRYFORFREEPROMO)
        try_free_promo.click()
        time.sleep(1)

    def download_block_wrapper(self):
        download_block = self.browser.find_element(*DownloadBlockLocators.DOWNLOADBLOCKWRAPPER)

    def email_for_start_promo(self):
        start_promo = self.browser.find_element(*DownloadBlockLocators.EMAILFORSTARTPROMOGROWTH)
        start_promo.send_keys("openmedia2020@mail.ru")

    def button_try_free_promo(self):
        free_promo = self.browser.find_element(*DownloadBlockLocators.BUTTONTRYFREEPROMOGROWTH)
        free_promo.click()

    def assept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()
        time.sleep(1)

    def close_promo_block(self):
        close_promo = self.browser.find_element(*DownloadBlockLocators.CLOSEPROMOBLOCK)
        close_promo.click()


