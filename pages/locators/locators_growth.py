from selenium.webdriver.common.by import By


class MainPageLocators:
# Локаторы кнопок на старнице growth
    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")
    GROWTH = (By.ID, "0")
    ADVANCED = (By.ID, "1")
    GENDER = (By.ID, "2")
    MACHINE = (By.ID, "3")
    AUDIENCE = (By.ID, "4")
    REPETITIVE = (By.ID, "5")
    MULTIPLE = (By.ID, "6")
    IMGPERFORMANCESTATISTICS = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/growth-and-performance-statistics.fd361f044fe5.png"]')
    IMGDETECT = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/detect.8f8304495b27.png"]')
    TEXTFEATUREHEADING = (By.CSS_SELECTOR, ".h1.info__features-heading.features-list__heading")
    TEXTINFOFEATURELIST = (By.CSS_SELECTOR, ".info__features-text.features-list__text")
    IMGCHECKQUALITY = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/check-quality.7dbe523b2c69.png"]')
    IMGFINDTARGET = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/find-target-audience.f73c68f806af.png"]')
    IMGINFLUENCERS = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/find-instagram-influencers.9da317caf86e.png"]')
    IMGMANAGEACTIVITY = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/manage-activity.a37ccbaf5eb6.png"]')
    IMGSCHEDULERPROMO = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/scheduler-promo.5ccd09ab8ee6.png"]')
    OTHERLOGOPROMOSCHEDULER = (By.CSS_SELECTOR, ".other-product__logo.other-product__logo--scheduler")
    USERSFEEDBACK = (By.CSS_SELECTOR, ".resize.users-feedback__text.h1")
    USERSNAMEFEEDBACK = (By.CSS_SELECTOR, ".h2.users-feedback__h2")
    #ARROWBUTTONRIGHT = (By.CSS_SELECTOR, ".arrow-button.arrow-button--right.slick-arrow")
    #ARROWBUTTONLEFT = (By.XPATH, '//div[@class="arrow-button arrow-button--left slick-arrow"]')
    USERSTRUSTUS = (By.CSS_SELECTOR, ".h0.customers-info__title")
    NUMERIQUES = (By.CSS_SELECTOR, ".customers-info__logo.customers-info__logo--numeriques")
    SEJ = (By.CSS_SELECTOR, ".customers-info__logo.customers-info__logo--sej")
    FORBES = (By.CSS_SELECTOR, ".customers-info__logo.customers-info__logo--forbes")
    ONLINEMARKETING = (By.CSS_SELECTOR, ".customers-info__logo.customers-info__logo--online-marketing")
    PRODUCTHUNT = (By.CSS_SELECTOR, ".customers-info__logo.customers-info__logo--product-hunt")
    LINKREADALLPUBLICATION = (By.CSS_SELECTOR, ".link-with-arrow.link-with-arrow--primary-color.customers-info__link")
    LINKLEARNMORE = (By.CSS_SELECTOR, ".link-with-arrow.link-with-arrow--primary-color.info__features-link")
    LINKNEWSLEARNMORE = By.CSS_SELECTOR, ".news__text-element.link-with-arrow.link-with-arrow--primary-color"

class DownloadBlockLocators:
#Локаторы на блоке загрузки growth
    EMAILFORSTART = (By.CLASS_NAME, "download-block__input ")
    BUTTONTRYFREE = (By.CSS_SELECTOR, "span.link-with-arrow.link-with-arrow--primary-color.link-with-arrow--down-small:nth-child(2)")
    BUTTONTRYFORFREEPROMO = (By.CSS_SELECTOR, "span.link-with-arrow.link-with-arrow--primary-color.link-with-arrow--down-small:nth-child(1)")
    DOWNLOADBLOCKWRAPPER = (By.XPATH, '//*[@id="reminder-modal-growth"]/div')
    EMAILFORSTARTPROMOGROWTH = (By.XPATH, '//*[@id="reminder-modal-growth"]/div/div[2]/form/div/input[1]')
    BUTTONTRYFREEPROMOGROWTH = (By.XPATH, '//*[@id="reminder-modal-growth"]/div/div[2]/form/div/button/span[2]')
    CLOSEPROMOBLOCK = (By.XPATH, '//*[@id="reminder-modal-growth"]/a')

class OpenLinkLocators:
#Локаторы ссылок со страницы growth
    WATCHADEMO = (By.CSS_SELECTOR, ".button-v2.button-v2--dark.button-v2--no-shadow.product-promo__button.button-v2__text.button-v2__text--white.button-v2--center-text")
    FOLLOWYOUBACK = (By.XPATH, '/html/body/div[1]/section[4]/div/div/a')
    CHECKYOURINSTAGRAMAUDIENCWQUALITY = (By.XPATH, '/html/body/div[1]/section[5]/div/div/a')
    FINDINSTAGRAMINFLUENCERSFORTOURACCOUNT = (By.XPATH, '/html/body/div[1]/section[7]/div/div/a')
    MONITORAUDIENCEACTIVITYANDGROWTH = (By.XPATH, '/html/body/div[1]/section[8]/div/div/a')
    PLANINSTAGRAMPOSTSFORAUTOPUBLISHING = (By.XPATH, '/html/body/div[1]/section[12]/div/div/a')

