from pages.locators.locators_install_growth import InstallGrowthLocators
from pages.base_page import BasePage
import time

class AppInstalledGrowth(BasePage):

    def cookies_close(self):
        to_cookies_close = self.browser.find_element(*InstallGrowthLocators.COOKIES_CLOSE)
        to_cookies_close.click()

# APP INSTALLED
    def installed_logo(self):
        self.browser.find_element(*InstallGrowthLocators.INSTALLEDLOGO)

    def installed_heading(self):
        text = self.browser.find_element(*InstallGrowthLocators.INSTALLEDHEADING).text
        assert text == "Thanks for Installing Combin!"

    def installed_text(self):
        text = self.browser.find_element(*InstallGrowthLocators.INSTALLEDTEXT).text
        assert text == "Please spread the word about us in social networks"


    def twitter_link(self):
        link = self.browser.find_element(*InstallGrowthLocators.TWITTERLINK).get_attribute("href")
        assert link == "https://twitter.com/getcombin"

    def twitter_img(self):
        self.browser.find_element(*InstallGrowthLocators.TWITTERIMG)


    def reddit_link(self):
        link = self.browser.find_element(*InstallGrowthLocators.REDDITLINK).get_attribute("href")
        assert link == "https://www.reddit.com/r/combin/"

    def reddit_img(self):
        self.browser.find_element(*InstallGrowthLocators.REDDITIMG)


    def quora_link(self):
        link = self.browser.find_element(*InstallGrowthLocators.QUORALINK).get_attribute("href")
        assert link == "https://www.quora.com/q/bmkfpemhlvdjpceq"

    def quora_img(self):
        self.browser.find_element(*InstallGrowthLocators.QUORAIMG)


    def youtube_link(self):
        link = self.browser.find_element(*InstallGrowthLocators.YOUTUBELINK).get_attribute("href")
        assert link == "https://www.youtube.com/channel/UC8nABZVCIxdC7H1HEEIJHJA"

    def youtube_img(self):
        self.browser.find_element(*InstallGrowthLocators.YOUTUBEIMG)


    def linkedin_link(self):
        link = self.browser.find_element(*InstallGrowthLocators.LINKEDINLINK).get_attribute("href")
        assert link == "https://www.linkedin.com/company/combin"

    def linkedin_img(self):
        self.browser.find_element(*InstallGrowthLocators.LINKEDINIMG)

# HOW WORKS

class HowItWorksGrowth(BasePage):

    def cookies_close(self):
        to_cookies_close = self.browser.find_element(*InstallGrowthLocators.COOKIES_CLOSE)
        to_cookies_close.click()

    def how_it_works_heading(self):
        self.browser.find_element(*InstallGrowthLocators.HOWITWORKSHEADING)

    def open_search(self):
        self.browser.find_element(*InstallGrowthLocators.OPENSEARCH)

    def img_second(self):
        self.browser.find_element(*InstallGrowthLocators.IMGSECOND)

    def arrow_button_down_1(self):
        self.browser.find_element(*InstallGrowthLocators.ARROWBUTTONDOWN1).click()
        time.sleep(1)

    def start_searching(self):
        self.browser.find_element(*InstallGrowthLocators.STARTSEARCHING)

    def img_third(self):
        self.browser.find_element(*InstallGrowthLocators.IMGTHIRD)

    def arrow_button_down_2(self):
        self.browser.find_element(*InstallGrowthLocators.ARROWBUTTONDOWN2).click()
        time.sleep(1)

    def find_new_people(self):
        self.browser.find_element(*InstallGrowthLocators.FINDNEWPEOPLE)

    def img_fourth(self):
        self.browser.find_element(*InstallGrowthLocators.IMGFOURTH)

    def arrow_button_down_3(self):
        self.browser.find_element(*InstallGrowthLocators.ARROWBUTTONDOWN3).click()
        time.sleep(1)

    def perform_mass(self):
        self.browser.find_element(*InstallGrowthLocators.PERFORMMASS)

    def img_fifth(self):
        self.browser.find_element(*InstallGrowthLocators.IMGFIFTH)

    def arrow_button_down_4(self):
        self.browser.find_element(*InstallGrowthLocators.ARROWBUTTONDOWN4).click()
        time.sleep(1)

    def watch_uor_video(self):
        self.browser.find_element(*InstallGrowthLocators.WATCHOURVIDEO).get_attribute("href")

    def video_tutorial_preview(self):
        self.browser.find_element(*InstallGrowthLocators.VIDEOTUTORIALPREVIEW).click()

    def video_tutorial(self):
        self.browser.find_element(*InstallGrowthLocators.VIDEOTOTURIAL)

    def close_video(self):
        self.browser.find_element(*InstallGrowthLocators.CLOSEVIDEO).click()

    def arrow_button_up(self):
        self.browser.find_element(*InstallGrowthLocators.ARROWBUTTONUP).click()
        time.sleep(1)
