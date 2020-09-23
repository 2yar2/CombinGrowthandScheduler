from pages.base_page import BasePage
from pages.locators.locators_help_guides_navigation import LocatorsHelpGuidesNavigation
import time


class ProductHelpGuidesNavigation(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*LocatorsHelpGuidesNavigation.COOKIES_CLOSE)
        close.click()

# Navigation

    def getting_started_to_grow_instagram_with_combin(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.GETTINSTARTEDTOGROWINSTAGRAMWITHCOMBIN).get_attribute("href")
        assert href == 'https://www.combin.com/guide/getting-started-to-grow-instagram-with-combin/'

    def getting_started_to_plan_instagram_publications_with_combin_scheduler(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.GETTINSTARTEDTOPLANINSTAGRAMPUBLICATIONSWITHCOMBINSCHEDULER).get_attribute("href")
        assert href == 'https://www.combin.com/guide/getting-started-to-plan-instagram-publications-with-combin-scheduler/'

    def how_do_i_get_more_than_1000_search_results(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.HOWDOIGETMORETHAN1000SEARCHRESULTS).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-do-i-get-more-than-1000-search-results/'

    def what_are_combins_sorting_and_filtering_options_for_search_results(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.WHATARECOMBINSSORTINGANDFILTERINGOPTIONS).get_attribute("href")
        assert href == 'https://www.combin.com/guide/what-are-combins-sorting-and-filtering-options-for-search-results/'

    def how_to_use_advanced_filters_and_machine_learning_analysis(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.HOWTOUSEADVANCEDFILTERSANDMACHINELEARNINGANALYSIS).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-use-advanced-filters-and-machine-learning-analysis/'

    def how_to_add_instagram_accounts_to_combins_safe_list_in_batch(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.HOWTOADDINSTAGRAMACCOUNTTOCOMBINSSAFELISTINBATCH).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-add-instagram-accounts-to-combins-safe-list-in-batch/'

    def how_to_add_users_to_black_list_in_combin(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.HOWTOADDUSERSTOBLACKLISTINCOMBIN).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-add-users-to-black-list-in-combin/'

    def how_to_backup_combin_user_lists_search_and_task_history(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.HOWTOBACKUPCOMBINUSERLISTSSEARCHANDTASKHUSTORY).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-backup-combin-user-lists-search-and-task-history/'

    def where_to_find_unfollowed_users_in_combin(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.WHERETOFINDUNFOLLOWEDUSERSINCOMBIN).get_attribute("href")
        assert href == 'https://www.combin.com/guide/where-to-find-unfollowed-users-in-combin/'

    def how_to_export_users_lists_to_xls_csv(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.HOWTOEXPORTUSERSLISTTOXLSCSV).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-export-users-lists-to-xls-csv/'

    def how_to_find_the_application_folder(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.HOWTOFINDTHEAPPLICATIONFOLDER).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-find-the-application-folder/'

    def how_to_login_to_account_registered_through_facebook(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.HOWTOLIGINTOACCOUNTREGISTEREDTHROUGHFACEBOOK).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-login-to-account-registered-through-facebook/'

    def how_to_logout_without_losing_account_information(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.HOWTOLOGUOTWITHOUTLOSINGACCOUNTINFORMATION).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-logout-without-losing-account-information/'

    def application_icons_and_their_meanings(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.APPLICATIONICONSANDTHEIRMEANINGS).get_attribute("href")
        assert href == 'https://www.combin.com/guide/application-icons-and-their-meanings/'

    def application_keyboard_shortcuts(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.APPLICATIONKEYBOARDSHORTCUTS).get_attribute("href")
        assert href == 'https://www.combin.com/guide/application-keyboard-shortcuts/'

    def how_to_schedule_instagram_posts(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.HOWTOSCHEDULEINSTAGRAMPOSTS).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-schedule-instagram-posts/'

    def how_to_schedule_instagram_stories(self):
        href = self.browser.find_element(*LocatorsHelpGuidesNavigation.HOWTOSCHEDULEINSTAGRAMSTORIES).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-schedule-instagram-stories/'