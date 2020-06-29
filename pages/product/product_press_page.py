from pages.locators.locators_press import LocatorsPressPage
from pages.base_page import BasePage
import time


class ProductPress(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*LocatorsPressPage.COOKIES_CLOSE)
        close.click()
# Block 1
    def promo_title(self):
        self.browser.find_element(*LocatorsPressPage.PROMOTITLE)

    def promo_text(self):
        self.browser.find_element(*LocatorsPressPage.PROMOTEXT)

    def brand_assert(self):
        self.browser.find_element(*LocatorsPressPage.BRANDASSERT)

    def our_logo(self):
        self.browser.find_element(*LocatorsPressPage.OURLOGO)

    def our_logo_zip(self):
        href = self.browser.find_element(*LocatorsPressPage.OURLOGOZIP).get_attribute("href")
        assert href == 'https://static.combin.com/base/press/logo/combin_logo.fef3a116ee42.zip'

    def our_text_1(self):
        self.browser.find_element(*LocatorsPressPage.OURTEXT1)

    def press_download_logo_1(self):
        self.browser.find_element(*LocatorsPressPage.PRESSDOWNLOADLOGO1)

    def item_property_1(self):
        self.browser.find_element(*LocatorsPressPage.ITEMPROPERTY1)

    def block_grey_logo_blue_1(self):
        self.browser.find_element(*LocatorsPressPage.BLOCKGREYLOGOBLUE1)

    def block_blue_logo_white_1(self):
        self.browser.find_element(*LocatorsPressPage.BLOCKBLUELOGOWHITE1)

    def our_symbol(self):
        self.browser.find_element(*LocatorsPressPage.OURSYMBOL)

    def our_symbol_zip(self):
        href = self.browser.find_element(*LocatorsPressPage.OURSYMBOLZIP).get_attribute("href")
        assert href == 'https://static.combin.com/base/press/symbol/combin_symbol.86d14c4bc10f.zip'

    def our_text_2(self):
        self.browser.find_element(*LocatorsPressPage.OURTEXT2)

    def press_download_logo_2(self):
        self.browser.find_element(*LocatorsPressPage.PRESSDOWNLOADLOGO2)

    def item_property_2(self):
        self.browser.find_element(*LocatorsPressPage.ITEMPROPERTY2)

    def block_grey_logo_blue_2(self):
        self.browser.find_element(*LocatorsPressPage.BLOCKGREYLOGOBLUE2)

    def block_blue_logo_white_2(self):
        self.browser.find_element(*LocatorsPressPage.BLOCKBLUELOGOWHITE2)

# Block 2
    def screenshot_and_video(self):
        self.browser.find_element(*LocatorsPressPage.SCREENSHOTANDVIDEO)

    def video_get_start(self):
        self.browser.find_element(*LocatorsPressPage.VIDEOGETSTART)

    def product_combin_screenshot(self):
        self.browser.find_element(*LocatorsPressPage.PRODUCTCOMBINSCREENSHOT)

    def product_combin_screenshot_zip(self):
        href = self.browser.find_element(*LocatorsPressPage.PRODUCTCOMBINSCREENSHOTZIP).get_attribute("href")
        assert href == 'https://static.combin.com/base/press/screenshots/combin_screenshots.e0e94b35d461.zip'

    def download_media_kit(self):
        self.browser.find_element(*LocatorsPressPage.DOWNLOADALLMEDIAKIT)

    def download_media_kit_pdf(self):
        href = self.browser.find_element(*LocatorsPressPage.DOWNLOADALLMEDIAKITPDF).get_attribute("href")
        assert href == 'https://static.combin.com/base/press/media-kit/combin_media_kit.35983e76b179.pdf'

# Press
    def recent_press(self):
        self.browser.find_element(*LocatorsPressPage.RECENTPRESS)

    def viev_more(self):
        self.browser.find_element(*LocatorsPressPage.VIEVMORE).click()

    def jyoti_chauhan(self):
        href = self.browser.find_element(*LocatorsPressPage.JYOTICHAUHAN).get_attribute("href")
        assert href == 'https://www.updateland.com/save-instagram-photos-pc/'

    def hasseb_ahmad(self):
        href = self.browser.find_element(*LocatorsPressPage.HASSEBAHMAD).get_attribute("href")
        assert href == 'https://twitgoo.com/grow-instagram-account-organically/'

    def eduardo_morales(self):
        href = self.browser.find_element(*LocatorsPressPage.EDUARDOMORALES).get_attribute("href")
        assert href == 'https://hackernoon.com/the-best-instagram-bot-that-will-keep-your-account-safe-4aaf0ccaee4d'

    def snighda(self):
        href = self.browser.find_element(*LocatorsPressPage.SNIGDHA).get_attribute("href")
        assert href == 'https://www.techpout.com/combin-scheduler-review/'

    def canberk_arinci(self):
        href = self.browser.find_element(*LocatorsPressPage.CANBERKARINCI).get_attribute("href")
        assert href == 'https://digitalagencynetwork.com/how-to-schedule-instagram-posts-and-stories/'

    def parampreet_chanana(self):
        href = self.browser.find_element(*LocatorsPressPage.PARAMPREETCHANANA).get_attribute("href")
        assert href == 'https://www.reviewsxp.com/blog/combin-review/'

    def john_paul_aguair(self):
        href = self.browser.find_element(*LocatorsPressPage.JOHNPAULAGUIAR).get_attribute("href")
        assert href == 'https://www.johnpaulaguiar.com/combin-review-instagram-marketing-tool/'

    def shanebarker(self):
        href = self.browser.find_element(*LocatorsPressPage.SHANEBARKER).get_attribute("href")
        assert href == 'https://shanebarker.com/blog/instagram-marketing-tools/'