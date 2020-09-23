from pages.base_page import BasePage
from pages.locators.locators_help_main_page import LocatorsHelpMain
import time


class ProductHelpMainPage(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*LocatorsHelpMain.COOKIES_CLOSE)
        close.click()

    def help_main_heading(self):
        self.browser.find_element(*LocatorsHelpMain.HELPMAINHEADING)

    def help_main_text(self):
        self.browser.find_element(*LocatorsHelpMain.HELPMAINTEXT)

    def navigation_guides(self):
        self.browser.find_element(*LocatorsHelpMain.NAVIGATIONGUIDES)

    def navigation_howto(self):
        self.browser.find_element(*LocatorsHelpMain.NAVIGATIONHOWTO)

    def navigation_faq(self):
        self.browser.find_element(*LocatorsHelpMain.NAVIGATIONFAQ)

    def navigation_troubleshooting(self):
        self.browser.find_element(*LocatorsHelpMain.NAVIGATIONTROUBLESHOOTING)

# Section Essential
    def essential(self):
        self.browser.find_element(*LocatorsHelpMain.ESSENTIAL)

    def getting_started_to_grow(self):
        href = self.browser.find_element(*LocatorsHelpMain.GETTINGSTARTEDTOGROW).get_attribute("href")
        assert href == 'https://www.combin.com/guide/getting-started-to-grow-instagram-with-combin/'

    def getting_started_to_grow_text(self):
        self.browser.find_element(*LocatorsHelpMain.GETTINGSTARTEDTOGROWTEXT)

    def getting_started_to_grow_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.GETTINGSTARTEDTOGROWSYMBOL)

    def getting_started_to_plan(self):
        href = self.browser.find_element(*LocatorsHelpMain.GETTINGSTARTEDTOPLAN).get_attribute("href")
        assert href == 'https://www.combin.com/guide/getting-started-to-plan-instagram-publications-with-combin-scheduler/'

    def getting_started_to_plan_text(self):
        self.browser.find_element(*LocatorsHelpMain.GETTINGSTARTEDTOPLANTEXT)

    def getting_starter_to_plan_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.GETTINGSTARTEDTOPLANSYMBOL)

    def is_combin_safe(self):
        href = self.browser.find_element(*LocatorsHelpMain.ISCOMBINSAFE).get_attribute("href")
        assert href == 'https://www.combin.com/faq/is-combin-safe-for-my-instagram-account/'

    def is_combin_safe_text(self):
        self.browser.find_element(*LocatorsHelpMain.ISCOMBINSAFETEXT)

    def is_combin_safe_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.ISCOMBINSAFESYMBOL)


#Section Search

    def search(self):
        self.browser.find_element(*LocatorsHelpMain.SEARCH)

    def how_do_i_get_more(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWDOIGETMORE).get_attribute("href")
        assert href == 'https://www.combin.com/faq/faq-how-do-i-get-more-than-1000-search-results/'

    def how_do_i_get_more_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWDOIGETMORETEXT)

    def how_do_i_get_more_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWDOIGETMORESYMBOL)

    def what_are_sorting(self):
        href = self.browser.find_element(*LocatorsHelpMain.WHATARESORTING).get_attribute("href")
        assert href == 'https://www.combin.com/guide/what-are-combins-sorting-and-filtering-options-for-search-results/'

    def what_are_sorting_text(self):
        self.browser.find_element(*LocatorsHelpMain.WHATARESORTINGTEXT)

    def what_are_sorting_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.WHATARESORTINGSYMBOL)

    def how_to_use_advanced(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOUSEADVANCED).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-use-advanced-filters-and-machine-learning-analysis/'

    def how_to_use_advanced_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOUSEADVANCEDTEXT)

    def how_to_use_advanced_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOUSEADVANCEDSYMBOL)

#Section User

    def user(self):
        self.browser.find_element(*LocatorsHelpMain.USER)

    def how_to_add_instagram(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOADDINSTAGRAM).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-add-instagram-accounts-to-combins-safe-list-in-batch/'

    def how_to_add_instagram_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOADDINSTAGRAMTEXT)

    def how_to_add_instagram_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOADDINSTAGRAMSYMBOL)

    def how_to_add_users_to_blacklict(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOADDUSERSTOBLACKLICT).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-add-users-to-black-list-in-combin/'

    def how_to_add_users_to_blacklist_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOADDUSERSTOBLACKLICTTEXT)

    def how_to_add_users_to_blacklist_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOADDUSERSTOBLACKLICTSYMBOL)

    def how_to_backup_combin(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOBACKUPCOMBIN).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-backup-combin-user-lists-search-and-task-history/'

    def how_to_backup_combin_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOBACKUPCOMBINTEXT)

    def how_to_backup_combin_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOBACKUPCOMBINSYMBOL)

    def where_to_find_unfollowers(self):
        href = self.browser.find_element(*LocatorsHelpMain.WHERETOFINDUNFOLLOWERS).get_attribute("href")
        assert href == 'https://www.combin.com/guide/where-to-find-unfollowed-users-in-combin/'

    def where_to_find_unfollowers_text(self):
        self.browser.find_element(*LocatorsHelpMain.WHERETOFINDUNFOLLOWERSTEXT)

    def where_to_find_unfollowers_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.WHERETOFINDUNFOLLOWERSSYMBOL)

    def how_to_export_users(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOEXPOTRUSERS).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-export-users-lists-to-xls-csv/'

    def how_to_export_users_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOEXPOTRUSERSTEXT)

    def how_to_export_users_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOEXPOTRUSERSSYMBOL)

#Section Login

    def login(self):
        self.browser.find_element(*LocatorsHelpMain.LOGIN)

    def how_to_logout(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOLOGOUT).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-logout-without-losing-account-information/'

    def how_to_logout_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOLOGOUTTEXT)

    def how_to_logout_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOLOGOUTSYMBOL)

    def how_to_login_account(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOLOGINTOACCOUNT).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-login-to-account-registered-through-facebook/'

    def how_to_login_account_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOLOGINTOACCOUNTTEXT)

    def how_to_login_account_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOLOGINTOACCOUNTSYMBOL)

    def how_to_find_the_application(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOFINDTHEAPPLICATION).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-find-the-application-folder/'

    def how_to_find_the_application_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOFINDTHEAPPLICATIONTEXT)

    def how_to_find_the_application_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOFINDTHEAPPLICATIONSYMBOL)

#Section General

    def general(self):
        self.browser.find_element(*LocatorsHelpMain.GENERAL)

    def application_keyboard(self):
        href = self.browser.find_element(*LocatorsHelpMain.APPLICATIONKEYBOARD).get_attribute("href")
        assert href == 'https://www.combin.com/guide/application-keyboard-shortcuts/'

    def application_keyboard_text(self):
        self.browser.find_element(*LocatorsHelpMain.APPLICATIONKEYBOARDTEXT)

    def application_keyboard_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.APPLICATIONKEYBOARDSYMBOL)

    def application_icons(self):
        href = self.browser.find_element(*LocatorsHelpMain.APPLICATIONICONS).get_attribute("href")
        assert href == 'https://www.combin.com/guide/application-icons-and-their-meanings/'

    def application_icon_text(self):
        self.browser.find_element(*LocatorsHelpMain.APPLICATIONICONSTEXT)

    def application_icon_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.APPLICATIONICONSSYMBOL)

#Section HowTo

    def howto(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTO)

    def howto_unfollowings_instagram_users(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOUNFOLLOWINSTAGRAMUSERS).get_attribute("href")
        assert href == 'https://www.combin.com/howto/how-to-unfollow-instagram-users-who-dont-follow-you-back/'

    def howto_unfollowings_instagram_users_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOUNFOLLOWINSTAGRAMUSERSTEXT)

    def howto_unfollowings_instagram_users_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOUNFOLLOWINSTAGRAMUSERSSYMBOL)

    def howto_find_and_engage(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOFINDANDENGAGE).get_attribute("href")
        assert href == 'https://www.combin.com/howto/how-to-find-and-engage-instagram-competitors-audience/'

    def howto_find_and_engage_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOFINDANDENGAGETEXT)

    def howto_find_and_engage_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOFINDANDENGAGESYMBOL)

    def howto_distinguish_real_followers(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTODISTINGUISHREALFOLLOWERS).get_attribute("href")
        assert href == 'https://www.combin.com/howto/how-to-distinguish-real-followers-of-your-instagram-account-with-combin/'

    def howto_distinguish_real_followers_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTODISTINGUISHREALFOLLOWERSTEXT)

    def howto_distinguish_real_followers_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTODISTINGUISHREALFOLLOWERSSYMBOL)

    def howto_find_your_target_audience(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOFINDYOURTARGETAUDIENCE).get_attribute("href")
        assert href == 'https://www.combin.com/howto/how-to-find-your-target-audience-on-instagram/'

    def howto_find_your_target_audience_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOFINDYOURTARGETAUDIENCETEXT)

    def howto_find_your_target_audience_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOFINDYOURTARGETAUDIENCESYMBOL)

    def howto_find_influencers(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOFINDINFLUENCERS).get_attribute("href")
        assert href == 'https://www.combin.com/howto/how-to-find-influencers-for-your-instagram-account/'

    def howto_find_influencers_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOFINDINFLUENCERSTEXT)

    def howto_find_influencers_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOFINDINFLUENCERSSYMBOL)

    def howto_interact(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOINTERACT).get_attribute("href")
        assert href == 'https://www.combin.com/howto/how-to-interact-with-followers-on-instagram-efficiently/'

    def howto_interact_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOFINDINFLUENCERSTEXT)

    def howto_interact_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOFINDINFLUENCERSSYMBOL)

    def howto_safely(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOSAFELY).get_attribute("href")
        assert href == 'https://www.combin.com/howto/safely-and-effectively-mass-comment-on-instagram/'

    def howto_safely_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOSAFELYTEXT)

    def howto_safely_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOSAFELYSYMBOL)

    def howto_leave_multiple_instagram(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOLEAVEMULTIPLEINSTAGRAM).get_attribute("href")
        assert href == 'https://www.combin.com/howto/how-to-leave-multiple-instagram-comments-with-different-text-in-batch/'

    def howto_leave_multiple_instagram_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOLEAVEMULTIPLEINSTAGRAMTEXT)

    def howto_leave_multiple_instagram_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOLEAVEMULTIPLEINSTAGRAMSYMBOL)

    def howto_automate_instagram_activity(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOAUTOMATEINSTAGRAMACTIVITY).get_attribute("href")
        assert href == 'https://www.combin.com/howto/automate-instagram-activity-without-getting-banned/'

    def howto_automate_instagram_activity_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOAUTOMATEINSTAGRAMACTIVITYTEXT)

    def howto_automate_instagram_activity_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOAUTOMATEINSTAGRAMACTIVITYSYMBOL)

    def howto_get_instagram_account(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOGETINSTAGRAMACCOUNT).get_attribute("href")
        assert href == 'https://www.combin.com/howto/how-to-get-instagram-account-statistics-and-track-audience-growth/'

    def howto_get_instagram_account_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOGETINSTAGRAMACCOUNTTEXT)

    def howto_get_instagram_account_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOGETINSTAGRAMACCOUNTSYMBOL)

    def howto_setup_instagram_hashtags(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOSETUPINSTAGRAMHASHTAGS).get_attribute("href")
        assert href == 'https://www.combin.com/howto/how-to-setup-instagram-hashtags-tracking/'

    def howto_setup_instagram_hashtags_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOSETUPINSTAGRAMHASHTAGSTEXT)

    def howto_setup_instagram_hashtags_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOSETUPINSTAGRAMHASHTAGSSYMBOL)

    def howto_sort_and_filter_search(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOSORTANDFILTERSEARCH)

    def howto_sort_and_filter_search_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOSORTANDFILTERSEARCHTEXT)

    def howto_sort_and_filter_search_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOSORTANDFILTERSEARCHSYMBOL)

    def howto_use_advanced_filters(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOUSEADVANCEDFILTERS).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-use-advanced-filters-and-machine-learning-analysis/'

    def howto_use_advanced_filters_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOUSEADVANCEDFILTERSTEXT)

    def howto_use_advanced_filters_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOUSEADVANCEDFILTERSSYMBOL)

    def howto_scheduler_instagram_posts(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOSCHEDULERINSTAGRAMPOSTS).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-schedule-instagram-posts/'

    def howto_scheduler_instagram_posts_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOSCHEDULERINSTAGRAMPOSTSTEXT)

    def howto_scheduler_instagram_posts_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOSCHEDULERINSTAGRAMPOSTSSYMBOL)

    def howto_scheduler_instagram_stories(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOSCHEDULERINSTAGRAMSTORIES).get_attribute("href")
        assert href == 'https://www.combin.com/guide/how-to-schedule-instagram-stories/'

    def howto_scheduler_instagram_stories_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOSCHEDULERINSTAGRAMSTORIESTEXT)

    def howto_scheduler_instagram_stories_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOSCHEDULERINSTAGRAMSTORIESSYMBOL)

    def howto_repost_instagram(self):
        href = self.browser.find_element(*LocatorsHelpMain.HOWTOREPOSTONINSTAGRAM).get_attribute("href")
        assert href == 'https://www.combin.com/howto/how-to-repost-on-instagram/'

    def howto_repost_instagram_text(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOREPOSTONINSTAGRAMTEXT)

    def howto_repost_instagram_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.HOWTOREPOSTONINSTAGRAMSYMBOL)


#Section FAQ

    def faq(self):
        self.browser.find_element(*LocatorsHelpMain.FAQ)

    def will_grow(self):
        href = self.browser.find_element(*LocatorsHelpMain.WILLITGROW).get_attribute("href")
        assert href == 'https://www.combin.com/faq/faq-will-it-grow-my-audience-automatically/'

    def will_grow_text(self):
        self.browser.find_element(*LocatorsHelpMain.WILLITGROWTEXT)

    def will_grow_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.WILLITGROWSYMBOL)

    def what_are_action_limits(self):
        href = self.browser.find_element(*LocatorsHelpMain.WHATAREACTIONLIMITS).get_attribute("href")
        assert href == 'https://www.combin.com/faq/faq-what-are-action-limits/'

    def what_are_action_limits_text(self):
        self.browser.find_element(*LocatorsHelpMain.WHATAREACTIONLIMITSTEXT)

    def what_are_action_limits_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.WHATAREACTIONLIMITSSYMBOL)

    def does_combin_support(self):
        href = self.browser.find_element(*LocatorsHelpMain.DOESCOMBINSUPPORT).get_attribute("href")
        assert href == 'https://www.combin.com/faq/faq-does-combin-support-instagram-two-factor-authentication/'

    def does_combin_support_text(self):
        self.browser.find_element(*LocatorsHelpMain.DOESCOMBINSUPPORTTEXT)

    def does_combin_support_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.DOESCOMBINSUPPORTSYMBOL)

    def what_is_safe_list(self):
        href = self.browser.find_element(*LocatorsHelpMain.WHATISSAFELIST).get_attribute("href")
        assert href == 'https://www.combin.com/faq/faq-what-is-safe-list/'

    def what_is_safe_list_text(self):
        self.browser.find_element(*LocatorsHelpMain.WHATISSAFELISTTEXT)

    def what_is_safe_list_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.WHATISSAFELISTSYMBOL)

    def what_are_the_hardware(self):
        href = self.browser.find_element(*LocatorsHelpMain.WHATARETHEHARDWARE).get_attribute("href")
        assert href == 'https://www.combin.com/faq/faq-what-are-the-hardware-and-operating-system-requirements/'

    def what_are_the_hardware_text(self):
        self.browser.find_element(*LocatorsHelpMain.WHATARETHEHARDWARETEXT)

    def what_are_the_hardware_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.WHATARETHEHARDWARESYMBOL)

    def does_it_work(self):
        href = self.browser.find_element(*LocatorsHelpMain.DOESITWORK).get_attribute("href")
        assert href == 'https://www.combin.com/faq/faq-does-it-work-when-computer-is-off-or-in-sleep-mode/'

    def does_it_work_text(self):
        self.browser.find_element(*LocatorsHelpMain.DOESITWORKTEXT)

    def does_it_work_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.DOESITWORKSYMBOL)

    def what_are_the_irrelevant(self):
        href = self.browser.find_element(*LocatorsHelpMain.WHATARETHEIRRELEVANT).get_attribute("href")
        assert href == 'https://www.combin.com/faq/faq-what-are-the-irrelevant-users/'

    def what_are_the_irrelevant_text(self):
        self.browser.find_element(*LocatorsHelpMain.WHATARETHEIRRELEVANTTEXT)

    def what_are_the_irrelevant_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.WHATARETHEIRRELEVANTSYMBOL)

    def where_to_find_proxy(self):
        href = self.browser.find_element(*LocatorsHelpMain.WHERETOFINDPROXY).get_attribute("href")
        assert href == 'https://www.combin.com/faq/faq-where-to-find-proxy/'

    def where_to_find_proxy_text(self):
        self.browser.find_element(*LocatorsHelpMain.WHERETOFINDPROXYTEXT)

    def where_to_find_proxy_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.WHERETOFINDPROXYSYMBOL)

    def where_do_i_get_starter_plan(self):
        href = self.browser.find_element(*LocatorsHelpMain.WHEREDOIGETTHESTARTERPLAN).get_attribute("href")
        assert href == 'https://www.combin.com/faq/faq-where-do-I-get-the-starter-plan-activation-key/'

    def where_do_i_get_starter_plan_text(self):
        self.browser.find_element(*LocatorsHelpMain.WHEREDOIGETTHESTARTERPLANTEXT)

    def where_do_i_get_starter_plan_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.WHEREDOIGETTHESTARTERPLANSYMBOL)

# Section Troubleshooting

    def troubleshooting(self):
        self.browser.find_element(*LocatorsHelpMain.TROUBLESHOOTING)

    def commenting_task_stuck(self):
        self.browser.find_element(*LocatorsHelpMain.COMMENTINGTASKSSTUCK).get_attribute("href")
        'https://www.combin.com/troubleshooting/troubleshooting-commenting-tasks-stuck-or-commenting-activity-significantly-dropped/'

    def commenting_task_stuck_text(self):
        self.browser.find_element(*LocatorsHelpMain.COMMENTINGTASKSSTUCKTEXT)

    def commenting_task_stuck_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.COMMENTINGTASKSSTUCKSYMBOL)

    def profile_and_users(self):
        self.browser.find_element(*LocatorsHelpMain.PROFILEANDUSERS).get_attribute("href")
        'https://www.combin.com/troubleshooting/profile-and-users-information-is-not-updated-or-displayed/'

    def profile_and_users_text(self):
        self.browser.find_element(*LocatorsHelpMain.PROFILEANDUSERSTEXT)

    def profile_and_users_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.PROFILEANDUSERSSYMBOL)

    def search_results(self):
        self.browser.find_element(*LocatorsHelpMain.SEARCHRESULTS).get_attribute("href")
        'https://www.combin.com/troubleshooting/troubleshooting-search-results-are-not-generating/'

    def search_results_text(self):
        self.browser.find_element(*LocatorsHelpMain.SEARCHRESULTSTEXT)

    def search_results_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.SEARCHRESULTSSYMBOL)

    def the_application_loading(self):
        self.browser.find_element(*LocatorsHelpMain.THEAPPLICATIONISLOADING).get_attribute("href")
        'https://www.combin.com/troubleshooting/troubleshooting-the-application-is-loading-data-for-too-long/'

    def the_application_loading_text(self):
        self.browser.find_element(*LocatorsHelpMain.THEAPPLICATIONISLOADINGTEXT)

    def the_application_loading_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.THEAPPLICATIONISLOADINGSYMBOL)

    def the_application_returns(self):
        self.browser.find_element(*LocatorsHelpMain.THEAPPLICATIONRETURNS).get_attribute("href")
        'https://www.combin.com/troubleshooting/troubleshooting-the-application-returns-error-1-how-to-fix-it/'

    def the_application_returns_text(self):
        self.browser.find_element(*LocatorsHelpMain.THEAPPLICATIONRETURNSTEXT)

    def the_application_returns_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.THEAPPLICATIONRETURNSSYMBOL)

    def action_task_spending(self):
        self.browser.find_element(*LocatorsHelpMain.ACTIONTASKSPENDING).get_attribute("href")
        'https://www.combin.com/troubleshooting/troubleshooting-action-tasks-pending-for-more-than-24-hours/'

    def action_task_spending_text(self):
        self.browser.find_element(*LocatorsHelpMain.ACTIONTASKSPENDINGTEXT)

    def action_task_spending_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.ACTIONTASKSPENDINGSYMBOL)

    def two_factor_authentication_code(self):
        self.browser.find_element(*LocatorsHelpMain.TWOFACTORAUTHENTICATIONCODES).get_attribute("href")
        'https://www.combin.com/troubleshooting/troubleshooting-two-factor-authentication-codes-are-not-accepted/'

    def two_factor_authentication_code_text(self):
        self.browser.find_element(*LocatorsHelpMain.TWOFACTORAUTHENTICATIONCODESTEXT)

    def two_factor_authentication_code_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.TWOFACTORAUTHENTICATIONCODESSYMBOL)

    def why_do_i_see_waiting_for_instagram_callback(self):
        self.browser.find_element(*LocatorsHelpMain.WHYDOISEEWAITINGFORINSTAGRAMCALLBACK).get_attribute("href")
        'https://www.combin.com/troubleshooting/why-do-i-see-waiting-for-instagram-callback-message/'

    def why_do_i_see_waiting_for_instagram_callback_text(self):
        self.browser.find_element(*LocatorsHelpMain.WHYDOISEEWAITINGFORINSTAGRAMCALLBACKTEXT)

    def why_do_i_see_waiting_for_instagram_callback_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.WHYDOISEEWAITINGFORINSTAGRAMCALLBACKSYMBOL)

    def why_di_i_see_following_limit_reached(self):
        self.browser.find_element(*LocatorsHelpMain.WHYDOISEEFOLLOWINGLIMITREACHED).get_attribute("href")
        'https://www.combin.com/troubleshooting/why-do-i-see-following-limit-reached-message/'

    def why_di_i_see_following_limit_reached_text(self):
        self.browser.find_element(*LocatorsHelpMain.WHYDOISEEFOLLOWINGLIMITREACHEDTEXT)

    def why_di_i_see_following_limit_reached_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.WHYDOISEEFOLLOWINGLIMITREACHEDSYMBOL)

    def why_are_not_action_processed(self):
        self.browser.find_element(*LocatorsHelpMain.WHYARENOTACTIONSPROCESSED).get_attribute("href")
        'https://www.combin.com/troubleshooting/why-arent-actions-processed-instantly/'

    def why_are_not_action_processed_text(self):
        self.browser.find_element(*LocatorsHelpMain.WHYARENOTACTIONSPROCESSEDTEXT)

    def why_are_not_action_processed_symbol(self):
        self.browser.find_element(*LocatorsHelpMain.WHYARENOTACTIONSPROCESSEDSYMBOL)