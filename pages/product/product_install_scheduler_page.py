from pages.locators.locators_install_scheduler import InstallSchedulerLocators
from pages.base_page import BasePage

class AppInstalledScheduler(BasePage):

    def cookies_close(self):
        to_cookies_close = self.browser.find_element(*InstallSchedulerLocators.COOKIES_CLOSE)
        to_cookies_close.click()

    def installed_logo(self):
        self.browser.find_element(*InstallSchedulerLocators.INSTALLEDLOGO)

    def installed_heading(self):
        text = self.browser.find_element(*InstallSchedulerLocators.INSTALLEDHEADING).text
        assert text == "Thanks for Installing Combin Scheduler!"

    def installed_text(self):
        text = self.browser.find_element(*InstallSchedulerLocators.INSTALLEDTEXT).text
        assert text == "Please spread the word about us in social networks"


    def twitter_link(self):
        link = self.browser.find_element(*InstallSchedulerLocators.TWITTERLINK).get_attribute("href")
        assert link == "https://twitter.com/getcombin"

    def twitter_img(self):
        self.browser.find_element(*InstallSchedulerLocators.TWITTERIMG)


    def reddit_link(self):
        link = self.browser.find_element(*InstallSchedulerLocators.REDDITLINK).get_attribute("href")
        assert link == "https://www.reddit.com/r/combin/"

    def reddit_img(self):
        self.browser.find_element(*InstallSchedulerLocators.REDDITIMG)


    def quora_link(self):
        link = self.browser.find_element(*InstallSchedulerLocators.QUORALINK).get_attribute("href")
        assert link == "https://www.quora.com/q/bmkfpemhlvdjpceq"

    def quora_img(self):
        self.browser.find_element(*InstallSchedulerLocators.QUORAIMG)


    def youtube_link(self):
        link = self.browser.find_element(*InstallSchedulerLocators.YOUTUBELINK).get_attribute("href")
        assert link == "https://www.youtube.com/channel/UC8nABZVCIxdC7H1HEEIJHJA"

    def youtube_img(self):
        self.browser.find_element(*InstallSchedulerLocators.YOUTUBEIMG)


    def linkedin_link(self):
        link = self.browser.find_element(*InstallSchedulerLocators.LINKEDINLINK).get_attribute("href")
        assert link == "https://www.linkedin.com/company/combin"

    def linkedin_img(self):
        self.browser.find_element(*InstallSchedulerLocators.LINKEDINIMG)

