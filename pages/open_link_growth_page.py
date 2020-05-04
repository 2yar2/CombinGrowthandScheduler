import time
from .base_page import BasePage
from .locators_growth import OpenLinkLocators
from .locators_growth import MainPageLocators


class OpenLinkWithGrowthPage(BasePage):

    def cookies_close(self):
        to_cookies_close = self.browser.find_element(*MainPageLocators.COOKIES_CLOSE)
        to_cookies_close.click()


    def watch_a_demo_video(self):
        watch_demo = self.browser.find_element(*OpenLinkLocators.WATCHADEMO)
        watch_demo.click()
        time.sleep(1)
        href = self.browser.find_element(*OpenLinkLocators.WATCHADEMO).get_attribute("href")
        print(href)


    def open_learn_more_growth_page(self):
        learn_more_follow_you_back = self.browser.find_element(*OpenLinkLocators.FOLLOWYOUBACK)
        learn_more_follow_you_back.click()

        learn_more_check_your_instagram_audience_quality = self.browser.find_element(*OpenLinkLocators.CHECKYOURINSTAGRAMAUDIENCWQUALITY)
        learn_more_check_your_instagram_audience_quality.click()

        find_instagram_influencers_for_your_account = self.browser.find_element(*OpenLinkLocators.FINDINSTAGRAMINFLUENCERSFORTOURACCOUNT)
        find_instagram_influencers_for_your_account.click()

        monitor_audience_activity_and_growth = self.browser.find_element(*OpenLinkLocators.MONITORAUDIENCEACTIVITYANDGROWTH)
        monitor_audience_activity_and_growth.click()

        plan_instagram_posts_for_auto_publishing = self.browser.find_element(*OpenLinkLocators.PLANINSTAGRAMPOSTSFORAUTOPUBLISHING)
        plan_instagram_posts_for_auto_publishing.click()

