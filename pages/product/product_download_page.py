from pages.locators.locators_download import LocatorsDownloadPage
from pages.base_page import BasePage
import time

class ProductDownloadPage(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*LocatorsDownloadPage.COOKIES_CLOSE)
        close.click()

    def download_heading(self):
        self.browser.find_element(*LocatorsDownloadPage.DOWNLOADHEADING)

# GROWTH
    def switch_growth(self):
        self.browser.find_element(*LocatorsDownloadPage.SWITCHGROWTH)

    def product_logo_growth(self):
        self.browser.find_element(*LocatorsDownloadPage.PRODUCTLOGOGROWTH)

    def version_element_growth(self):
        self.browser.find_element(*LocatorsDownloadPage.VERSIONELEMENTGROWTH)

    def version_info(self):
        self.browser.find_element(*LocatorsDownloadPage.VERSIONINFO)

# DOWNLOAD OS GROWTH
#win32
    def download_os_win32(self):
        os = self.browser.find_element(*LocatorsDownloadPage.DOWNLOADOS)
        os.click()

    def icon_win32(self):
        self.browser.find_element(*LocatorsDownloadPage.ICONWIN32)

    def text_win32(self):
        self.browser.find_element(*LocatorsDownloadPage.TEXTWIN32).click()

    def download_button_win32(self):
        self.browser.find_element(*LocatorsDownloadPage.DOWNLOADBUTTON).click()
        time.sleep(1)

#win64

    def download_os_win64(self):
        os = self.browser.find_element(*LocatorsDownloadPage.DOWNLOADOS)
        os.click()

    def icon_win64(self):
        self.browser.find_element(*LocatorsDownloadPage.ICONWIN64)

    def text_win64(self):
        self.browser.find_element(*LocatorsDownloadPage.TEXTWIN64).click()

    def download_button_win64(self):
        self.browser.find_element(*LocatorsDownloadPage.DOWNLOADBUTTON).click()
        time.sleep(1)

#macOS

    def download_os_macos(self):
        os = self.browser.find_element(*LocatorsDownloadPage.DOWNLOADOS)
        os.click()

    def icon_macos(self):
        self.browser.find_element(*LocatorsDownloadPage.ICONMACOS)

    def text_macos(self):
        self.browser.find_element(*LocatorsDownloadPage.TEXTMACOS).click()

    def download_button_macos(self):
        self.browser.find_element(*LocatorsDownloadPage.DOWNLOADBUTTON)
        time.sleep(1)

#ubuntu

    def download_os_ubuntu(self):
        os = self.browser.find_element(*LocatorsDownloadPage.DOWNLOADOS)
        os.click()

    def icon_ubuntu(self):
        self.browser.find_element(*LocatorsDownloadPage.ICONUBUNTU)

    def text_ubuntu(self):
        self.browser.find_element(*LocatorsDownloadPage.TEXTUBUNTU).click()

    def download_button_ubuntu(self):
        self.browser.find_element(*LocatorsDownloadPage.DOWNLOADBUTTON)
        time.sleep(1)

    def release_date(self):
        self.browser.find_element(*LocatorsDownloadPage.RELEASEDATE)

    def system_requirments(self):
        text = self.browser.find_element(*LocatorsDownloadPage.SYSTEMREQUIREMENTS).text
        assert text == "The application is supported on Windows 8 and newer, Mac OS 10.13 and newer, and Ubuntu 18.04 and newer (64-bit only)."

# DOWNLOAD OS SCHEDULER

    def switch_scheduler(self):
        self.browser.find_element(*LocatorsDownloadPage.SWITCHSCHEDULER).click()

    def product_logo_scheduler(self):
        self.browser.find_element(*LocatorsDownloadPage.PRODUCTLOGOSCHEDULER)

    def version_element_scheduler(self):
        self.browser.find_element(*LocatorsDownloadPage.VERSIONELEMENTSCHEDULER)

