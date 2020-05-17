from .locators_scheduler import SchedulerPageLocators
from .locators_growth import DownloadBlockLocators
from .base_page import BasePage
import time


class ProductPageScheduler(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*SchedulerPageLocators.COOKIES_CLOSE)
        close.click()

    def ahead_posting(self):
        aheadposting = self.browser.find_element(*SchedulerPageLocators.AHEAD)
        assert self.is_element_present(*SchedulerPageLocators.AHEAD), "Plan and schedule Instagram posts for later or upload new publications immediately. We support both."
        aheadposting.click()

    def auto_publishing(self):
        autopublishing = self.browser.find_element(*SchedulerPageLocators.AUTOMATEDPUBLISHING)
        assert self.is_element_present(*SchedulerPageLocators.AUTOMATEDPUBLISHING), "Upload images, select a publishing date and you are good to go. No annoying reminders to post, Combin does all publishing for you."
        autopublishing.click()

    def imgsize(self):
        imgsize = self.browser.find_element(*SchedulerPageLocators.IMAGESIZE)
        assert self.is_element_present(*SchedulerPageLocators.IMAGESIZE), "Fit your images to the aspect ratios Instagram supports using the crop and zoom features. Change the size to square, vertical, portrait and landscape right in the app."
        imgsize.click()

    def loc_tag(self):
        loctag = self.browser.find_element(*SchedulerPageLocators.LOCATIONTAGGING)
        assert self.is_element_present(*SchedulerPageLocators.LOCATIONTAGGING), "Specify relevant locations for your posts to attract Instagram accounts from your area."
        loctag.click()

    def hashtag_accountmentioning(self):
        hashtagaccount = self.browser.find_element(*SchedulerPageLocators.HASHTAGSACCOUNTSMENTIONING)
        assert self.is_element_present(*SchedulerPageLocators.HASHTAGSACCOUNTSMENTIONING), "Use hashtags and tag other accounts in the post captions to grab attention and drive more engagement."
        hashtagaccount.click()

    def bulk_stories(self):
        bulkstories = self.browser.find_element(*SchedulerPageLocators.BULKSTORIES)
        assert self.is_element_present(*SchedulerPageLocators.BULKSTORIES), "Select one, a couple or a whole handful of images and schedule them in one click to be published in your Instagram Stories."
        bulkstories.click()

    def img_carousel(self):
        self.browser.find_element(*SchedulerPageLocators.IMGCAROUSEL)

    def img_save_time(self):
        self.browser.find_element(*SchedulerPageLocators.IMGSAVETIMEFLEXIBLE)

    def heading_save_time(self):
        self.browser.find_element(*SchedulerPageLocators.HEADINGSAVETIMEPOSTSSCHEDULING)

    def text_save_time(self):
        self.browser.find_element(*SchedulerPageLocators.TEXTSAVETIMEPOSTSSHEDULING)

    def img_create_dozens(self):
        self.browser.find_element(*SchedulerPageLocators.IMGCREATEDOZENS)

    def heading_create_dozens(self):
        self.browser.find_element(*SchedulerPageLocators.HEADINGCREATEDOZENS)

    def text_create_dozens(self):
        self.browser.find_element(*SchedulerPageLocators.TEXTCREATEDOZENS)

    def img_style_instagram_grid(self):
        self.browser.find_element(*SchedulerPageLocators.IMGSTYLEINSTAGRAMGRIL)

    def heading_style_instagram_grid(self):
        self.browser.find_element(*SchedulerPageLocators.HEADINGSTYLEINSTAGRAMGRIL)

    def text_style_instagram_grid(self):
        self.browser.find_element(*SchedulerPageLocators.TEXTSTYLEINSTAGRAMGRIL)

    def img_manage_grow_audience(self):
        self.browser.find_element(*SchedulerPageLocators.IMGMANAGEGROWAUDIENCE)

    def heading_manage_grow_audience(self):
        self.browser.find_element(*SchedulerPageLocators.HEADINGMANAGEGROWAUDIENCE)

    def link_manage_grow_audience(self):
        self.browser.find_element(*SchedulerPageLocators.LINKMANAGEGROWAUDIENCE)

class ProductPromoScheduler(BasePage):

    def cookies_close(self):
        to_cookies_close = self.browser.find_element(*SchedulerPageLocators.COOKIES_CLOSE)
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
        start_promo = self.browser.find_element(*SchedulerPageLocators.EMAILFORSTARTPROMOSCHEDULER)
        start_promo.send_keys("openmedia@mail.ru")

    def button_try_free_promo(self):
        free_promo = self.browser.find_element(*SchedulerPageLocators.BUTTONTRYFREEPROMOSCHEDULER)
        free_promo.click()

    def assept_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()
        time.sleep(1)

    def close_promo_block(self):
        close_promo = self.browser.find_element(*SchedulerPageLocators.DOWNLOADBLOCKCLOSE)
        close_promo.click()
