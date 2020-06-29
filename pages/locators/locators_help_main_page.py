from selenium.webdriver.common.by import By

class LocatorsHelpMain:

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")

    ANNOUNCEMENT = (By.XPATH, '/html/body/div[1]/section[1]/div[1]/a')

    HELPMAINHEADING = (By.CSS_SELECTOR, '.h1.help-main__heading.help-main__heading--top')
    HELPMAINTEXT = (By.CSS_SELECTOR, '.help-main__text.h2')

    NAVIGATIONGUIDES = (By.XPATH, '/html/body/div[1]/section[1]/div[3]/a[1]') #href="https://www.combin.com/help/#gettingstarted"
    NAVIGATIONHOWTO = (By.XPATH, '/html/body/div[1]/section[1]/div[3]/a[2]') #https://www.combin.com/help/#howto
    NAVIGATIONFAQ = (By.XPATH, '/html/body/div[1]/section[1]/div[3]/a[3]')#https://www.combin.com/help/#faq
    NAVIGATIONTROUBLESHOOTING = (By.XPATH, '/html/body/div[1]/section[1]/div[3]/a[4]')#https://www.combin.com/help/#troubleshooting
# Section Essential
    ESSENTIAL = (By.XPATH, '/html/body/div[1]/section[2]/div/div/h2')

    GETTINGSTARTEDTOGROW = (By.XPATH, '/html/body/div[1]/section[2]/div/ul/li[1]/a')#https://www.combin.com/guide/getting-started-to-grow-instagram-with-combin/
    GETTINGSTARTEDTOGROWTEXT = (By.XPATH, '/html/body/div[1]/section[2]/div/ul/li[1]/a/p')
    GETTINGSTARTEDTOGROWSYMBOL = (By.XPATH, '/html/body/div[1]/section[2]/div/ul/li[1]/a/span')

    GETTINGSTARTEDTOPLAN = (By.XPATH, '/html/body/div[1]/section[2]/div/ul/li[2]/a') #https://www.combin.com/guide/getting-started-to-plan-instagram-publications-with-combin-scheduler/
    GETTINGSTARTEDTOPLANTEXT = (By.XPATH, '/html/body/div[1]/section[2]/div/ul/li[2]/a/p')
    GETTINGSTARTEDTOPLANSYMBOL = (By.XPATH, '/html/body/div[1]/section[2]/div/ul/li[2]/a/span')

    ISCOMBINSAFE = (By.XPATH, '/html/body/div[1]/section[2]/div/ul/li[3]/a') #https://www.combin.com/faq/is-combin-safe-for-my-instagram-account/
    ISCOMBINSAFETEXT = (By.XPATH, '/html/body/div[1]/section[2]/div/ul/li[3]/a/p')
    ISCOMBINSAFESYMBOL = (By.XPATH, '/html/body/div[1]/section[2]/div/ul/li[3]/a/span')
# Section Search
    SEARCH = (By.XPATH, '/html/body/div[1]/section[3]/div/div/h2')

    HOWDOIGETMORE = (By.XPATH, '/html/body/div[1]/section[3]/div/ul/li[1]/a')#https://www.combin.com/guide/how-do-i-get-more-than-1000-search-results/
    HOWDOIGETMORETEXT = (By.XPATH, '/html/body/div[1]/section[3]/div/ul/li[1]/a/p')
    HOWDOIGETMORESYMBOL = (By.XPATH, '/html/body/div[1]/section[3]/div/ul/li[1]/a/span')

    WHATARESORTING = (By.XPATH, '/html/body/div[1]/section[3]/div/ul/li[2]/a') #https://www.combin.com/guide/what-are-combins-sorting-and-filtering-options-for-search-results/
    WHATARESORTINGTEXT = (By.XPATH, '/html/body/div[1]/section[3]/div/ul/li[2]/a/p')
    WHATARESORTINGSYMBOL = (By.XPATH, '/html/body/div[1]/section[3]/div/ul/li[2]/a/span')

    HOWTOUSEADVANCED = (By.XPATH, '/html/body/div[1]/section[3]/div/ul/li[3]/a')#https://www.combin.com/guide/how-to-use-advanced-filters-and-machine-learning-analysis/
    HOWTOUSEADVANCEDTEXT = (By.XPATH, '/html/body/div[1]/section[3]/div/ul/li[3]/a/p')
    HOWTOUSEADVANCEDSYMBOL = (By.XPATH, '/html/body/div[1]/section[3]/div/ul/li[3]/a/span')
# Section User
    USER = (By.XPATH, '/html/body/div[1]/section[4]/div/div/h2')

    HOWTOADDINSTAGRAM = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[1]/li[1]/a')#https://www.combin.com/guide/how-to-add-instagram-accounts-to-combins-safe-list-in-batch/
    HOWTOADDINSTAGRAMTEXT = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[1]/li[1]/a/p')
    HOWTOADDINSTAGRAMSYMBOL = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[1]/li[1]/a/span')

    HOWTOADDUSERSTOBLACKLICT = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[1]/li[2]/a')#https://www.combin.com/guide/how-to-add-users-to-black-list-in-combin/
    HOWTOADDUSERSTOBLACKLICTTEXT = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[1]/li[2]/a/p')
    HOWTOADDUSERSTOBLACKLICTSYMBOL = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[1]/li[2]/a/span')

    HOWTOBACKUPCOMBIN = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[2]/li[1]/a')#https://www.combin.com/guide/how-to-backup-combin-user-lists-search-and-task-history/
    HOWTOBACKUPCOMBINTEXT = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[2]/li[1]/a/p')
    HOWTOBACKUPCOMBINSYMBOL = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[2]/li[1]/a/span')

    WHERETOFINDUNFOLLOWERS = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[2]/li[2]/a')#https://www.combin.com/guide/where-to-find-unfollowed-users-in-combin/
    WHERETOFINDUNFOLLOWERSTEXT = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[2]/li[2]/a/p')
    WHERETOFINDUNFOLLOWERSSYMBOL = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[2]/li[2]/a/span')

    HOWTOEXPOTRUSERS = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[2]/li[3]/a')#https://www.combin.com/guide/how-to-export-users-lists-to-xls-csv/
    HOWTOEXPOTRUSERSTEXT = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[2]/li[3]/a/p')
    HOWTOEXPOTRUSERSSYMBOL = (By.XPATH, '/html/body/div[1]/section[4]/div/ul[2]/li[3]/a/span')
# Section Login
    LOGIN = (By.XPATH, '/html/body/div[1]/section[5]/div/div/h2')

    HOWTOLOGINTOACCOUNT = (By.XPATH, '/html/body/div[1]/section[5]/div/ul/li[1]/a')#https://www.combin.com/guide/how-to-login-to-account-registered-through-facebook/
    HOWTOLOGINTOACCOUNTTEXT = (By.XPATH, '/html/body/div[1]/section[5]/div/ul/li[1]/a/p')
    HOWTOLOGINTOACCOUNTSYMBOL = (By.XPATH, '/html/body/div[1]/section[5]/div/ul/li[1]/a/span')

    HOWTOLOGOUT = (By.XPATH, '/html/body/div[1]/section[5]/div/ul/li[2]/a')#https://www.combin.com/guide/how-to-logout-without-losing-account-information/
    HOWTOLOGOUTTEXT = (By.XPATH, '/html/body/div[1]/section[5]/div/ul/li[2]/a/p')
    HOWTOLOGOUTSYMBOL = (By.XPATH, '/html/body/div[1]/section[5]/div/ul/li[2]/a/span')

    HOWTOFINDTHEAPPLICATION = (By.XPATH, '/html/body/div[1]/section[5]/div/ul/li[3]/a')#https://www.combin.com/guide/how-to-find-the-application-folder/
    HOWTOFINDTHEAPPLICATIONTEXT = (By.XPATH, '/html/body/div[1]/section[5]/div/ul/li[3]/a/p')
    HOWTOFINDTHEAPPLICATIONSYMBOL = (By.XPATH, '/html/body/div[1]/section[5]/div/ul/li[3]/a/span')
# Section General
    GENERAL = (By.XPATH, '/html/body/div[1]/section[6]/div/div/h2')

    APPLICATIONKEYBOARD = (By.XPATH, '/html/body/div[1]/section[6]/div/ul/li[1]/a')#https://www.combin.com/guide/application-keyboard-shortcuts/
    APPLICATIONKEYBOARDTEXT = (By.XPATH, '/html/body/div[1]/section[6]/div/ul/li[1]/a/p')
    APPLICATIONKEYBOARDSYMBOL = (By.XPATH, '/html/body/div[1]/section[6]/div/ul/li[1]/a/span')

    APPLICATIONICONS = (By.XPATH, '/html/body/div[1]/section[6]/div/ul/li[2]/a')#https://www.combin.com/guide/application-icons-and-their-meanings/
    APPLICATIONICONSTEXT = (By.XPATH, '/html/body/div[1]/section[6]/div/ul/li[2]/a/p')
    APPLICATIONICONSSYMBOL = (By.XPATH, '/html/body/div[1]/section[6]/div/ul/li[2]/a/span')

# Section HowTo
    HOWTO = (By.XPATH, '/html/body/div[1]/section[7]/div/div/h2')

    HOWTOUNFOLLOWINSTAGRAMUSERS = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[1]/li[1]/a')#https://www.combin.com/howto/how-to-unfollow-instagram-users-who-dont-follow-you-back/
    HOWTOUNFOLLOWINSTAGRAMUSERSTEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[1]/li[1]/a/p')
    HOWTOUNFOLLOWINSTAGRAMUSERSSYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[1]/li[1]/a/span')

    HOWTOFINDANDENGAGE = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[1]/li[2]/a')#https://www.combin.com/howto/how-to-find-and-engage-instagram-competitors-audience/
    HOWTOFINDANDENGAGETEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[1]/li[2]/a/p')
    HOWTOFINDANDENGAGESYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[1]/li[2]/a/span')

    HOWTODISTINGUISHREALFOLLOWERS = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[2]/li[1]/a')#https://www.combin.com/howto/how-to-distinguish-real-followers-of-your-instagram-account-with-combin/
    HOWTODISTINGUISHREALFOLLOWERSTEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[2]/li[1]/a/p')
    HOWTODISTINGUISHREALFOLLOWERSSYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[2]/li[1]/a/span')

    HOWTOFINDYOURTARGETAUDIENCE = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[2]/li[2]/a')#https://www.combin.com/howto/how-to-find-your-target-audience-on-instagram/
    HOWTOFINDYOURTARGETAUDIENCETEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[2]/li[2]/a/p')
    HOWTOFINDYOURTARGETAUDIENCESYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[2]/li[2]/a/span')

    HOWTOFINDINFLUENCERS = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[2]/li[3]/a')#https://www.combin.com/howto/how-to-find-influencers-for-your-instagram-account/
    HOWTOFINDINFLUENCERSTEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[2]/li[3]/a/p')
    HOWTOFINDINFLUENCERSSYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[2]/li[3]/a/span')

    HOWTOINTERACT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[2]/li[4]/a')#https://www.combin.com/howto/how-to-interact-with-followers-on-instagram-efficiently/
    HOWTOINTERACTTEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[2]/li[4]/a/p')
    HOWTOINTERACTSYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[2]/li[4]/a/span')

    HOWTOSAFELY = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[3]/li[1]/a')#https://www.combin.com/howto/safely-and-effectively-mass-comment-on-instagram/
    HOWTOSAFELYTEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[3]/li[1]/a/p')
    HOWTOSAFELYSYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[3]/li[1]/a/span')

    HOWTOLEAVEMULTIPLEINSTAGRAM = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[3]/li[2]/a')#https://www.combin.com/howto/how-to-leave-multiple-instagram-comments-with-different-text-in-batch/
    HOWTOLEAVEMULTIPLEINSTAGRAMTEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[3]/li[2]/a/p')
    HOWTOLEAVEMULTIPLEINSTAGRAMSYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[3]/li[2]/a/span')

    HOWTOAUTOMATEINSTAGRAMACTIVITY = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[3]/li[3]/a')#https://www.combin.com/howto/automate-instagram-activity-without-getting-banned/
    HOWTOAUTOMATEINSTAGRAMACTIVITYTEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[3]/li[3]/a/p')
    HOWTOAUTOMATEINSTAGRAMACTIVITYSYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[3]/li[3]/a/span')

    HOWTOGETINSTAGRAMACCOUNT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[4]/li[1]/a')#https://www.combin.com/howto/how-to-get-instagram-account-statistics-and-track-audience-growth/
    HOWTOGETINSTAGRAMACCOUNTTEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[4]/li[1]/a/p')
    HOWTOGETINSTAGRAMACCOUNTSYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[4]/li[1]/a/span')

    HOWTOSETUPINSTAGRAMHASHTAGS = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[4]/li[2]/a')#https://www.combin.com/howto/how-to-setup-instagram-hashtags-tracking/
    HOWTOSETUPINSTAGRAMHASHTAGSTEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[4]/li[2]/a/p')
    HOWTOSETUPINSTAGRAMHASHTAGSSYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[4]/li[2]/a/span')

    HOWTOSORTANDFILTERSEARCH = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[4]/li[3]/a')#https://www.combin.com/howto/how-to-sort-and-filter-search-results-in-combin/
    HOWTOSORTANDFILTERSEARCHTEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[4]/li[3]/a/p')
    HOWTOSORTANDFILTERSEARCHSYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[4]/li[3]/a/span')

    HOWTOUSEADVANCEDFILTERS = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[4]/li[4]/a')#https://www.combin.com/howto/how-to-use-advanced-filter-and-machine-learning-analysis/
    HOWTOUSEADVANCEDFILTERSTEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[4]/li[4]/a/p')
    HOWTOUSEADVANCEDFILTERSSYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[4]/li[4]/a/span')

    HOWTOSCHEDULERINSTAGRAMPOSTS = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[5]/li[1]/a')#https://www.combin.com/guide/how-to-schedule-instagram-posts/
    HOWTOSCHEDULERINSTAGRAMPOSTSTEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[5]/li[1]/a/p')
    HOWTOSCHEDULERINSTAGRAMPOSTSSYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[5]/li[1]/a/span')

    HOWTOSCHEDULERINSTAGRAMSTORIES = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[5]/li[2]/a')#https://www.combin.com/guide/how-to-schedule-instagram-stories/
    HOWTOSCHEDULERINSTAGRAMSTORIESTEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[5]/li[2]/a/p')
    HOWTOSCHEDULERINSTAGRAMSTORIESSYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[5]/li[2]/a/span')

    HOWTOREPOSTONINSTAGRAM = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[5]/li[3]/a')#https://www.combin.com/howto/how-to-repost-on-instagram/
    HOWTOREPOSTONINSTAGRAMTEXT = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[5]/li[3]/a/p')
    HOWTOREPOSTONINSTAGRAMSYMBOL = (By.XPATH, '/html/body/div[1]/section[7]/div/ul[5]/li[3]/a/span')

# Section FAQ
    FAQ = (By.XPATH, '/html/body/div[1]/section[8]/div/div/h2')

    WILLITGROW = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[1]/li[1]/a')#https://www.combin.com/faq/faq-will-it-grow-my-audience-automatically/
    WILLITGROWTEXT = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[1]/li[1]/a/p')
    WILLITGROWSYMBOL = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[1]/li[1]/a/span')

    WHATAREACTIONLIMITS = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[1]/li[2]/a')#https://www.combin.com/faq/faq-what-are-action-limits/
    WHATAREACTIONLIMITSTEXT = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[1]/li[2]/a/p')
    WHATAREACTIONLIMITSSYMBOL = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[1]/li[2]/a/span')

    DOESCOMBINSUPPORT = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[1]/li[3]/a')#https://www.combin.com/faq/faq-does-combin-support-instagram-two-factor-authentication/
    DOESCOMBINSUPPORTTEXT = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[1]/li[3]/a/p')
    DOESCOMBINSUPPORTSYMBOL = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[1]/li[3]/a/span')

    WHATISSAFELIST = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[2]/li[1]/a')#https://www.combin.com/faq/faq-what-is-safe-list/
    WHATISSAFELISTTEXT = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[2]/li[1]/a/p')
    WHATISSAFELISTSYMBOL = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[2]/li[1]/a/span')

    WHATARETHEHARDWARE = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[2]/li[2]/a')#https://www.combin.com/faq/faq-what-are-the-hardware-and-operating-system-requirements/
    WHATARETHEHARDWARETEXT = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[2]/li[2]/a/p')
    WHATARETHEHARDWARESYMBOL = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[2]/li[2]/a/span')

    DOESITWORK = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[2]/li[3]/a')#https://www.combin.com/faq/faq-does-it-work-when-computer-is-off-or-in-sleep-mode/
    DOESITWORKTEXT = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[2]/li[3]/a/p')
    DOESITWORKSYMBOL = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[2]/li[3]/a/span')

    WHATARETHEIRRELEVANT = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[3]/li[1]/a')#https://www.combin.com/faq/faq-what-are-the-irrelevant-users/
    WHATARETHEIRRELEVANTTEXT = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[3]/li[1]/a/p')
    WHATARETHEIRRELEVANTSYMBOL = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[3]/li[1]/a/span')

    WHERETOFINDPROXY = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[3]/li[2]/a')#https://www.combin.com/faq/faq-where-to-find-proxy/
    WHERETOFINDPROXYTEXT = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[3]/li[2]/a/p')
    WHERETOFINDPROXYSYMBOL = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[3]/li[2]/a/span')

    WHEREDOIGETTHESTARTERPLAN = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[3]/li[3]/a')#https://www.combin.com/faq/faq-where-do-I-get-the-starter-plan-activation-key/
    WHEREDOIGETTHESTARTERPLANTEXT = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[3]/li[3]/a/p')
    WHEREDOIGETTHESTARTERPLANSYMBOL = (By.XPATH, '/html/body/div[1]/section[8]/div/ul[3]/li[3]/a/span')

# Section Troubleshooting

    TROUBLESHOOTING = (By.XPATH, '/html/body/div[1]/section[9]/div/div/h2')

    COMMENTINGTASKSSTUCK = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[1]/li[1]/a')#https://www.combin.com/troubleshooting/troubleshooting-commenting-tasks-stuck-or-commenting-activity-significantly-dropped/
    COMMENTINGTASKSSTUCKTEXT = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[1]/li[1]/a/p')
    COMMENTINGTASKSSTUCKSYMBOL = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[1]/li[1]/a/span')

    PROFILEANDUSERS = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[1]/li[2]/a')#https://www.combin.com/troubleshooting/profile-and-users-information-is-not-updated-or-displayed/
    PROFILEANDUSERSTEXT = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[1]/li[2]/a/p')
    PROFILEANDUSERSSYMBOL = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[1]/li[2]/a/span')

    SEARCHRESULTS = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[1]/li[3]/a')#https://www.combin.com/troubleshooting/troubleshooting-search-results-are-not-generating/
    SEARCHRESULTSTEXT = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[1]/li[3]/a/p')
    SEARCHRESULTSSYMBOL = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[1]/li[3]/a/span')

    THEAPPLICATIONISLOADING = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[2]/li[1]/a')#https://www.combin.com/troubleshooting/troubleshooting-the-application-is-loading-data-for-too-long/
    THEAPPLICATIONISLOADINGTEXT = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[2]/li[1]/a/p')
    THEAPPLICATIONISLOADINGSYMBOL = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[2]/li[1]/a/span')

    THEAPPLICATIONRETURNS = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[2]/li[2]/a')#https://www.combin.com/troubleshooting/troubleshooting-the-application-returns-error-1-how-to-fix-it/
    THEAPPLICATIONRETURNSTEXT = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[2]/li[2]/a/p')
    THEAPPLICATIONRETURNSSYMBOL = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[2]/li[2]/a/span')

    ACTIONTASKSPENDING = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[2]/li[3]/a')#https://www.combin.com/troubleshooting/troubleshooting-action-tasks-pending-for-more-than-24-hours/
    ACTIONTASKSPENDINGTEXT = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[2]/li[3]/a/p')
    ACTIONTASKSPENDINGSYMBOL = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[2]/li[3]/a/span')

    TWOFACTORAUTHENTICATIONCODES = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[3]/li[1]/a')#https://www.combin.com/troubleshooting/troubleshooting-two-factor-authentication-codes-are-not-accepted/
    TWOFACTORAUTHENTICATIONCODESTEXT = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[3]/li[1]/a/p')
    TWOFACTORAUTHENTICATIONCODESSYMBOL = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[3]/li[1]/a/span')

    WHYDOISEEWAITINGFORINSTAGRAMCALLBACK = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[3]/li[2]/a')#https://www.combin.com/troubleshooting/why-do-i-see-waiting-for-instagram-callback-message/
    WHYDOISEEWAITINGFORINSTAGRAMCALLBACKTEXT = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[3]/li[2]/a/p')
    WHYDOISEEWAITINGFORINSTAGRAMCALLBACKSYMBOL = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[3]/li[2]/a/span')

    WHYDOISEEFOLLOWINGLIMITREACHED = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[3]/li[3]/a')#https://www.combin.com/troubleshooting/why-do-i-see-following-limit-reached-message/
    WHYDOISEEFOLLOWINGLIMITREACHEDTEXT = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[3]/li[3]/a/p')
    WHYDOISEEFOLLOWINGLIMITREACHEDSYMBOL = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[3]/li[3]/a/span')

    WHYARENOTACTIONSPROCESSED = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[3]/li[4]/a')#https://www.combin.com/troubleshooting/why-arent-actions-processed-instantly/
    WHYARENOTACTIONSPROCESSEDTEXT = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[3]/li[4]/a/p')
    WHYARENOTACTIONSPROCESSEDSYMBOL  = (By.XPATH, '/html/body/div[1]/section[9]/div/ul[3]/li[4]/a/span')
