from selenium.webdriver.common.by import By

class MainPageCombinLocators:

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")
    PRODUCTHEADLINE = (By.ID, "product-cards-headline")

# FIRST CARDS
    CARDGROWTH = (By.CSS_SELECTOR, ".product-card.product-card--growth.product-cards__card")
    CARDGROWTHCONTENT = (By.XPATH, '/html/body/div[1]/section[1]/div/div[2]/a[1]/div[1]/p')
    CARDGROWTHLOGO = (By.CSS_SELECTOR, ".product-card__logo.product-card__logo--growth.background-image.product-logo.product-logo--growth-white")

    CARDSCHEDULER = (By.CSS_SELECTOR, ".product-card.product-card--scheduler.product-cards__card")
    CARDSCHEDULERCONTENT = (By.XPATH, '/html/body/div[1]/section[1]/div/div[2]/a[2]/div[1]/p')
    CARDSCHEDULERLOGO = (By.CSS_SELECTOR, ".product-card__logo.product-card__logo--scheduler.background-image.product-logo.product-logo--scheduler-white")

    AVIALABLE = (By.CSS_SELECTOR, ".avaliable.avaliable--row")

    CANYOUDOWITHCOMBINHOMEHEADING = (By.XPATH, '/html/body/div[1]/section[2]/h2')
# CARD PRODUCT
    ATTRACTNEWINSTAGRAMFOLLOWERSTITLE = (By.XPATH, '/html/body/div[1]/section[2]/div/a[1]/h3')
    ATTRACTNEWINSTAGRAMFOLLOWERSTEXT = (By.XPATH, '/html/body/div[1]/section[2]/div/a[1]/p')
    ATTRACTNEWINSTAGRAMFOLLOWERSIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/card-images/attract-followers.06ec9e385dbe.png"]')

    PLANSCHEDULEINSTAGRAMCONTENTTITLE = (By.XPATH, '/html/body/div[1]/section[2]/div/a[2]/h3')
    PLANSCHEDULEINSTAGRAMCONTENTTEXT = (By.XPATH, '/html/body/div[1]/section[2]/div/a[2]/p')
    PLANSCHEDULEINSTAGRAMCONTENTIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/card-images/schedule-instagram.162075e648f8.png"]')

    MANAGEMULTIPLEACCOUNTSTITLE = (By.XPATH, '/html/body/div[1]/section[2]/div/a[3]/h3')
    MANAGEMULTIPLEACCOUNTSTEXT = (By.XPATH, '/html/body/div[1]/section[2]/div/a[3]/p')
    MANAGEMULTIPLEACCOUNTSIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/card-images/multiple-accounts.4c0a54a5b5f8.png"]')

    COMMUNICATEWHITYOURAUDIENCETITLE = (By.XPATH, '/html/body/div[1]/section[2]/div/a[4]/h3')
    COMMUNICATEWHITYOURAUDIENCETEXT = (By.XPATH, '/html/body/div[1]/section[2]/div/a[4]/p')
    COMMUNICATEWHITYOURAUDIENCEIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/card-images/communicate-audience.041d896037db.png"]')

    TRACKACTIVITYANDGROWTHTITLE = (By.XPATH, '/html/body/div[1]/section[2]/div/a[5]/h3')
    TRACKACTIVITYANDGROWTHTEXT = (By.XPATH, '/html/body/div[1]/section[2]/div/a[5]/p')
    TRACKACTIVITYANDGROWTHIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/card-images/track-activity.aa6b62d20bb0.png"]')

# iNFO CONTENT
    INFOTITLE = (By.CSS_SELECTOR, ".h0.customers-info__title")

    NUMERIQUES = (By.CSS_SELECTOR, ".customers-info__logos-container .customers-info__logo.customers-info__logo--numeriques")
    SEJ = (By.CSS_SELECTOR, ".customers-info__logos-container .customers-info__logo.customers-info__logo--sej")
    FORBES = (By.CSS_SELECTOR, ".customers-info__logos-container .customers-info__logo.customers-info__logo--forbes")
    ONLINEMARKETING = (By.CSS_SELECTOR, ".customers-info__logos-container .customers-info__logo.customers-info__logo--online-marketing")
    PRODUCTHUNT = (By.CSS_SELECTOR, ".customers-info__logos-container .customers-info__logo.customers-info__logo--product-hunt")

# FEEDBACK
    BRITTNEYFEEDBACK = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div/div[1]/div/div[1]/p')
    BRITTNEYINSTAGRAM = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div/div[1]/div/div[1]/a')             #get_attribute
    BRITTNEYUSERNAME = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div/div[1]/div/div[1]/a/p[1]')
    BRITTNEYIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/users-photo/brittney_jae_.png"]')

    NOWFORFREEHOMEHEADING = (By.XPATH, '/html/body/div[1]/section[5]/h2')

# CARD PRODUCT
    CARDGROWTHROUNDED = (By.XPATH, '/html/body/div[1]/section[5]/div/div[1]')
    CARDGROWTHBACKGROUNDLOGO = (By.CSS_SELECTOR, ".background-image.product-logo.product-logo--growth-primary.try-now__logo.try-now__logo--growth")
    CARDGROWTHBACKGROUNDHEADING = (By.XPATH, '/html/body/div[1]/section[5]/div/div[1]/h3')
    CARDGROWTHBACKGROUNDIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/growth-main-page.f52191c02d23.png"]')

    CARDSCHEDULERROUNDED = (By.XPATH, '/html/body/div[1]/section[5]/div/div[2]')
    CARDSCHEDULERBACKGROUNDLOGO = (By.XPATH, '/html/body/div[1]/section[5]/div/div[2]/span')
    CARDSCHEDULERBACKGROUNDHEADING = (By.XPATH, '/html/body/div[1]/section[5]/div/div[2]/h3')
    CARDSCHEDULERBACKGROUNDIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/scheduler-main-page.d6dfb7ad7677.png"]')

    OURLATESTNEWSHOMEHEADING = (By.XPATH, '/html/body/div[1]/section[6]/h2')

#BLOG
    BLOGCOMBINLEFTCARD = (By.XPATH, '/html/body/div[1]/section[6]/div/a[1]')
    BLOGCOMBINLEFTCARDIMG = (By.XPATH, '/html/body/div[1]/section[6]/div/a[1]/div[1]/img')
    BLOGCOMBINLEFTCARDTEXT = (By.XPATH, '/html/body/div[1]/section[6]/div/a[1]/div[2]/h3')

    BLOGCOMBINMEDIUMCARD = (By.XPATH, '/html/body/div[1]/section[6]/div/a[2]')
    BLOGCOMBINMEDIUMCARDIMG = (By.XPATH, '/html/body/div[1]/section[6]/div/a[2]/div[1]/img')
    BLOGCOMBINMEDIUMCARDTEXT = (By.XPATH, '/html/body/div[1]/section[6]/div/a[2]/div[2]/h3')

    BLOGCOMBINRIGHTCARD = (By.XPATH, '/html/body/div[1]/section[6]/div/a[3]')
    BLOGCOMBINRIGHTCARDIMG = (By.XPATH, '/html/body/div[1]/section[6]/div/a[3]/div[1]/img')
    BLOGCOMBINRIGHTCARDTEXT = (By.XPATH, '/html/body/div[1]/section[6]/div/a[3]/div[2]/h3')

# Открытие ссылок ПЕРВЫХ КАРТОЧЕК на ГЛАВНОЙ странице КОМБИН
    # FIRST CARD GROWTH
    CARDGROWTHBUTTONLEARNMORE = (By.XPATH, '/html/body/div[1]/section[1]/div/div[2]/a[1]/div[2]/div/p') #CLICK
    CARDGROWTHBUTTONTRYFORFREE = (By.XPATH, '/html/body/div[1]/section[1]/div/div[2]/a[1]/div[2]/button/p')

    DOWNLOADBLOCKGROWTHLOGO = (By.XPATH, '//*[@id="reminder-modal-growth"]/div/div[1]')
    DOWNLOADBLOCKGROWTHTEXT = (By.XPATH, '//*[@id="reminder-modal-growth"]/div/h3[1]')
    DOWNLOADBLOCKGROWTHINPUT = (By.XPATH, '//*[@id="reminder-modal-growth"]/div/div[2]/form/div/input[1]')
    DOWNLOADBLOCKGROWTHTRYFORFREE = (By.XPATH, '//*[@id="reminder-modal-growth"]/div/div[2]/form/div/button') #ALLERT
    DOWNLOADBLOCKGROWTHCLOSE = (By.XPATH, '//*[@id="reminder-modal-growth"]/a')
    # FIRST CARD SCHEDULER
    CARDSCHEDULERBUTTONLEARNMORE = (By.XPATH, '/html/body/div[1]/section[1]/div/div[2]/a[2]/div[2]/div/p') #CLICK
    CARDSCHEDULERBUTTONTRYFORFREE = (By.XPATH, '/html/body/div[1]/section[1]/div/div[2]/a[2]/div[2]/button/p')

    DOWNLOADBLOCKSCHEDULERLOGO = (By.XPATH, '//*[@id="reminder-modal-scheduler"]/div/div[1]')
    DOWNLOADBLOCKSCHEDULERTEXT = (By.XPATH, '//*[@id="reminder-modal-scheduler"]/div/h3[1]')
    DOWNLOADBLOCKSCHEDULERINPUT = (By.XPATH, '//*[@id="reminder-modal-scheduler"]/div/div[2]/form/div/input[1]')
    DOWNLOADBLOCKSCHEDULERTRYFORFREE = (By.XPATH, '//*[@id="reminder-modal-scheduler"]/div/div[2]/form/div/button/span[2]') #ALLERT

# Открытие ссылок на ГЛАВНОЙ странице КОМБИН

    CARDINSTAGRAMGROWTH = (By.XPATH, '/html/body/div[1]/section[2]/div/a[1]') #get_attribute
    CARDFREEINSTAGRAMSCHEDULER = (By.XPATH, '/html/body/div[1]/section[2]/div/a[2]')
    CARDINSTAGRAMGROWTHMANAGE = (By.XPATH, '/html/body/div[1]/section[2]/div/a[3]')
    CARDINSTAGRAMGROWTHCOMMUNICATE = (By.XPATH, '/html/body/div[1]/section[2]/div/a[4]')
    CARDINSTAGRAMGROWTHTRACK = (By.XPATH, '/html/body/div[1]/section[2]/div/a[5]')

    PRESS = (By.XPATH, '/html/body/div[1]/section[3]/div/a')

    FEEDBACKBUTTONRIGHT = (By.XPATH, '//*[@id="next-button"]')
    FEEDBACKBUTTONRIGHT2 = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div/div[2]/div/div[2]/div[2]/div[2]')
    FEEDBACKINSTAGRAMID = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div/div[3]/div/div[1]/a') #get_attribute


# rounded-block try-now__item combin and scheduler
    LASTDOWNLOADBLOCKGROWTHLEARNMORE = (By.XPATH, '/html/body/div[1]/section[5]/div/div[1]/div/div/a')
    LASTDOWNLOADBLOCKSCHEDULERLEARNMORE = (By.XPATH, '/html/body/div[1]/section[5]/div/div[2]/div/div/a')

    LASTDOWNLOADBLOCKGROWTHTRYFORFREE = (By.XPATH, '/html/body/div[1]/section[5]/div/div[1]/div/div/button/span')
    LASTDOWNLOADBLOCKGROWTHINPUT = (By.XPATH, '//*[@id="reminder-modal-growth"]/div/div[2]/form/div/input[1]')
    LASTDOWNLOADBLOCKGROWTHTRYFREE = (By.XPATH, '//*[@id="reminder-modal-growth"]/div/div[2]/form/div/button/span[2]')

    LASTDOWNLOADBLOCKSHEDULERTRYFORFREE = (By.XPATH, '/html/body/div[1]/section[5]/div/div[2]/div/div/button/span')
    LASTDOWNLOADBLOCKSCHEDULERINPUT = (By.XPATH, '//*[@id="reminder-modal-scheduler"]/div/div[2]/form/div/input[1]')
    LASTDOWNLOADBLOCKSHEDULERTRYFREE = (By.XPATH, '//*[@id="reminder-modal-scheduler"]/div/div[2]/form/div/button')