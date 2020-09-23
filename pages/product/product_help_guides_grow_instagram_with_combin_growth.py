from pages.base_page import BasePage
from pages.locators.locators_help_guides_grow_instagram_with_combin_growth import LocatorsHelpGuidesInstagramwithCombinGrowth
import time


class ProductHelpGuidesInstagramwithCombinGrowth(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.COOKIES_CLOSE)
        close.click()

# Assert LINK on page

    def activity_limits(self):
        href = self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.ACTIVITYLIMITS).get_attribute("href")
        assert href == 'https://www.combin.com/faq/faq-what-are-action-limits/'

    def main_product(self):
        href = self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.MAINPRODUCT).get_attribute("href")
        assert href == 'https://www.combin.com/product/instagram-growth/'

    def download_growth(self):
        href = self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.DOWNLOADGROWTH).get_attribute("href")
        assert href == 'https://download.combin.com/app/combin_2.6.2_x64.msi?source=website'

    def does_not_store_or_share_password(self):
        href = self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.DOESNOTSTOREORSHAREPASSWORDS).get_attribute("href")
        assert href == 'https://www.combin.com/privacy-policy/'

    def following_followers_ratio(self):
        href = self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.FOLLOWINGFOLLOWERSRATIO).get_attribute("href")
        assert href == 'https://workmacro.com/instagram/follower-following-ratio-say-instagram-account/'

    def display_purposes(self):
        href = self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.DISPLAYPURPOSES).get_attribute("href")
        assert href == 'https://displaypurposes.com/'

    def batch(self):
        href = self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.BATCH).get_attribute("href")
        assert href == 'https://www.combin.com/howto/how-to-leave-multiple-instagram-comments-with-different-text-in-batch/'

    def export_csv_xls(self):
        href = self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.EXPORTEDCSVANDXLS).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-export-users-lists-to-xls-csv/'

    def backup(self):
        href = self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.BACKUP).get_attribute("href")
        assert href == 'https://www.combin.com/howto/how-to-backup-combin-user-lists-search-and-task-history/'

# Assert IMG and VIDEO on page


    def youtube_video(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.YOUTUBEVIDEO)

    def img_loggining(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGLOGGINING)

    def img_profile(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGPROFILE)

    def img_activation(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGACTIVATION)

    def img_proxy_setup(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGPROXYSETUP)

    def img_search(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGSEARCH)

    def img_search_by_hashtag(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGSEARCHBYHASHTAG)

    def img_search_by_haschtag_2(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGSEARCHBYHASHTAG2)

    def img_location(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGLOCATION)

    def img_location_2(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGLOCATION2)

    def img_location_and_hashtag(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGLOCATIONANDHASHTAG)

    def img_user_search(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGUSERSEARCH)

    def img_user_search_2(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGUSERSEARCH2)

    def img_filtering(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGFILTERING)

    def img_advanced_filter(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGADVANCEDFILTER)

    def img_activities(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGACTIVITIES)

    def img_comment(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGCOMMENT)

    def img_audience_management(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGAUDIENCEMANAGEMENT)

    def img_tasks(self):
        self.browser.find_element(*LocatorsHelpGuidesInstagramwithCombinGrowth.IMGTASKS)