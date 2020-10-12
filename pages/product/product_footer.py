from pages.locators.locators_footer import LocatorsFooter
from pages.base_page import BasePage
import time


class FooterOnMainPage(BasePage):

    def cookies_close(self):
        to_cookies_close = self.browser.find_element(*LocatorsFooter.COOKIES_CLOSE)
        to_cookies_close.click()

    def aria_label(self):
        self.browser.find_element(*LocatorsFooter.ARIALABEL)

    def footer_copyright(self):
        self.browser.find_element(*LocatorsFooter.FOOTERCOPYRIGHT)

    def blog_combin(self):
        blog = self.browser.find_element(*LocatorsFooter.BLOGCOMBIN).get_attribute("href")
        assert blog == "https://blog.combin.com/"

    def twitter_combin(self):
        twitter = self.browser.find_element(*LocatorsFooter.TWITTERCOMBIN).get_attribute("href")
        assert twitter == "https://twitter.com/getcombin"

    def youtube_combin(self):
        youtube = self.browser.find_element(*LocatorsFooter.YOUTUBECOMBIN).get_attribute("href")
        assert youtube == "https://www.youtube.com/channel/UC8nABZVCIxdC7H1HEEIJHJA"

    def reddit_combin(self):
        reddit = self.browser.find_element(*LocatorsFooter.REDDITCOMBIN).get_attribute("href")
        assert reddit == "https://reddit.com/r/combin"

#PRODUCT
    def product(self):
        self.browser.find_element(*LocatorsFooter.PRODUCT)

    def product_growth(self):
        growth = self.browser.find_element(*LocatorsFooter.PRODUCTGROWTH).get_attribute("href")
        assert growth == "https://www.combin.com/product/instagram-growth/"
        text = self.browser.find_element(*LocatorsFooter.PRODUCTGROWTH).text
        assert text == "Growth"

    def product_scheduler(self):
        scheduler = self.browser.find_element(*LocatorsFooter.PRODUCTSCHEDULER).get_attribute("href")
        assert scheduler == "https://www.combin.com/product/free-instagram-scheduler/"
        text = self.browser.find_element(*LocatorsFooter.PRODUCTSCHEDULER).text
        assert text == "Scheduler"

    def product_aidaform(self):
        aidaform = self.browser.find_element(*LocatorsFooter.PRODUCTAIDAFORM).get_attribute("href")
        assert aidaform == "https://www.combin.com/aidaform/"
        text = self.browser.find_element(*LocatorsFooter.PRODUCTAIDAFORM).text
        assert text == "Aidaform"

    def product_instacheck(self):
        instacheck = self.browser.find_element(*LocatorsFooter.PRODUCTINSTACHECK).get_attribute("href")
        assert instacheck == "https://www.combin.com/instacheck/"
        text = self.browser.find_element(*LocatorsFooter.PRODUCTINSTACHECK).text
        assert text == "InstaCheck"

    def product_pricing(self):
        pricing = self.browser.find_element(*LocatorsFooter.PRODUCTPRICING).get_attribute("href")
        assert pricing == "https://www.combin.com/pricing/"
        text = self.browser.find_element(*LocatorsFooter.PRODUCTPRICING).text
        assert text == "Pricing"

    def product_download(self):
        download = self.browser.find_element(*LocatorsFooter.PRODUCTDOWNLOAD).get_attribute("href")
        assert download == "https://www.combin.com/download/"
        text = self.browser.find_element(*LocatorsFooter.PRODUCTDOWNLOAD).text
        assert text == "Download"

#COMPANY

    def company(self):
        self.browser.find_element(*LocatorsFooter.COMPANY)

    def company_about(self):
        about = self.browser.find_element(*LocatorsFooter.COMPANYABOUT).get_attribute("href")
        assert about == "https://www.combin.com/about/"
        text = self.browser.find_element(*LocatorsFooter.COMPANYABOUT).text
        assert text == "About"

    def company_blog(self):
        blog = self.browser.find_element(*LocatorsFooter.COMPANYBLOG).get_attribute("href")
        assert blog == "https://blog.combin.com/"
        text = self.browser.find_element(*LocatorsFooter.COMPANYBLOG).text
        assert text == "Blog"

    def company_roadmap(self):
        roadmap = self.browser.find_element(*LocatorsFooter.COMPANYROADMAP).get_attribute("href")
        assert roadmap == "https://trello.com/b/9IgHtpBg/combin-product-roadmap"
        text = self.browser.find_element(*LocatorsFooter.COMPANYROADMAP).text
        assert text == "Roadmap"

    def company_affiliate(self):
        affiliate = self.browser.find_element(*LocatorsFooter.COMPANYAFFILIATE).get_attribute("href")
        assert affiliate == "https://www.combin.com/affiliate-program/"
        text = self.browser.find_element(*LocatorsFooter.COMPANYAFFILIATE).text
        assert text == "Affiliate"

    def company_press(self):
        press = self.browser.find_element(*LocatorsFooter.COMPANYPRESS).get_attribute("href")
        assert press == "https://www.combin.com/press/"
        text = self.browser.find_element(*LocatorsFooter.COMPANYPRESS).text
        assert text == "Press"

#HELP

    def help(self):
        self.browser.find_element(*LocatorsFooter.HELP)

    def help_guides(self):
        guides = self.browser.find_element(*LocatorsFooter.HELPGUIDES).get_attribute("href")
        assert guides == "https://www.combin.com/help/#gettingstarted"
        text = self.browser.find_element(*LocatorsFooter.HELPGUIDES).text
        assert text == "Guides"

    def help_how_to(self):
        howto = self.browser.find_element(*LocatorsFooter.HELPHOWTO).get_attribute("href")
        assert howto == "https://www.combin.com/help/#howto"
        text = self.browser.find_element(*LocatorsFooter.HELPHOWTO).text
        assert text == "How To"

    def help_faq(self):
        faq = self.browser.find_element(*LocatorsFooter.HELPFAQ).get_attribute("href")
        assert faq == "https://www.combin.com/help/#faq"
        text = self.browser.find_element(*LocatorsFooter.HELPFAQ).text
        assert text == "FAQ"

    def help_troubleshooting(self):
        troubleshooting = self.browser.find_element(*LocatorsFooter.HELPTROUBLESHOOTING).get_attribute("href")
        assert troubleshooting == "https://www.combin.com/help/#troubleshooting"
        text = self.browser.find_element(*LocatorsFooter.HELPTROUBLESHOOTING).text
        assert text == "Troubleshooting"

#USE CASES

    def use_cases(self):
        self.browser.find_element(*LocatorsFooter.USECASES)

    def use_cases_detected(self):
        detected = self.browser.find_element(*LocatorsFooter.USECASESDETECTED).get_attribute("href")
        assert detected == "https://www.combin.com/howto/how-to-unfollow-instagram-users-who-dont-follow-you-back/"
        text = self.browser.find_element(*LocatorsFooter.USECASESDETECTED).text
        assert text == "Detect Who Doesn’t Follow You Back"

    def use_cases_find(self):
        find = self.browser.find_element(*LocatorsFooter.USECASESFIND).get_attribute("href")
        assert find == "https://www.combin.com/product/instagram-growth/#audience"
        text = self.browser.find_element(*LocatorsFooter.USECASESFIND).text
        assert text == "Find Target Audience on Instagram"

    def use_cases_check(self):
        check = self.browser.find_element(*LocatorsFooter.USECASESCHECK).get_attribute("href")
        assert check == "https://www.combin.com/howto/how-to-distinguish-real-followers-of-your-instagram-account-with-combin/"
        text = self.browser.find_element(*LocatorsFooter.USECASESCHECK).text
        assert text == "Check Your Instagram Audience Quality"

    def use_cases_save(self):
        save = self.browser.find_element(*LocatorsFooter.USECASESSAVE).get_attribute("href")
        assert save == "https://www.combin.com/product/free-instagram-scheduler/"
        text = self.browser.find_element(*LocatorsFooter.USECASESSAVE).text
        assert text == "Save Time with Flexible Posts Scheduling"




