from selenium.webdriver.common.by import By

class LocatorsPressPage:

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")

    PROMOTITLE = (By.CSS_SELECTOR, ".h1.h1--white.press__promo-title")
    PROMOTEXT = (By.CSS_SELECTOR, ".h2.h2--white.press__promo-text")
# Block 1
    BRANDASSERT = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div/h3')

    OURLOGO = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/ul/li[1]/div[1]')
    OURLOGOZIP = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/ul/li[1]/div[1]/a') #href="https://static.combin.com/base/press/logo/combin_logo.fef3a116ee42.zip"
    OURTEXT1 = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/ul/li[1]/div[1]/a/p')
    PRESSDOWNLOADLOGO1 = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/ul/li[1]/div[1]/a/div/span')
    ITEMPROPERTY1 = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/ul/li[1]/div[1]/a/div/p')

    BLOCKGREYLOGOBLUE1 = (By.CSS_SELECTOR, ".help-section__item.press-block.press-block--grey.press-block--logo-blue")
    BLOCKBLUELOGOWHITE1 = (By.CSS_SELECTOR, ".help-section__item.press-block.press-block--blue.press-block--logo-white")


    OURSYMBOL = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/ul/li[2]/div[1]')
    OURSYMBOLZIP = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/ul/li[2]/div[1]/a')#href="https://static.combin.com/base/press/symbol/combin_symbol.86d14c4bc10f.zip"
    OURTEXT2 = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/ul/li[2]/div[1]/a/p')
    PRESSDOWNLOADLOGO2 = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/ul/li[2]/div[1]/a/div/span')
    ITEMPROPERTY2 = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/ul/li[2]/div[1]/a/div/p')

    BLOCKGREYLOGOBLUE2 = (By.CSS_SELECTOR, ".help-section__item.press-block.press-block--grey.press-block--symbol")
    BLOCKBLUELOGOWHITE2 = (By.CSS_SELECTOR, ".help-section__item.press-block.press-block--blue.press-block--symbol")
# Block 2
    SCREENSHOTANDVIDEO = (By.XPATH, '/html/body/div[1]/section[2]/div[2]/div/h3')

    VIDEOGETSTART = (By.XPATH, '/html/body/div[1]/section[2]/div[2]/ul/li[1]/a/p')
    PRODUCTCOMBINSCREENSHOT = (By.XPATH, '/html/body/div[1]/section[2]/div[2]/ul/li[2]')
    PRODUCTCOMBINSCREENSHOTZIP = (By.XPATH, '/html/body/div[1]/section[2]/div[2]/ul/li[2]/a')#href="https://static.combin.com/base/press/screenshots/combin_screenshots.e0e94b35d461.zip"
    DOWNLOADALLMEDIAKIT = (By.XPATH, '/html/body/div[1]/section[2]/div[2]/ul/li[3]')
    DOWNLOADALLMEDIAKITPDF = (By.XPATH, '/html/body/div[1]/section[2]/div[2]/ul/li[3]/a')#href="https://static.combin.com/base/press/media-kit/combin_media_kit.35983e76b179.pdf"
# Press
    RECENTPRESS = (By.CSS_SELECTOR, ".help-section__heading.press-release__headline.h1")

    VIEVMORE = (By.CSS_SELECTOR, ".h2.h2--primary-color.press-release__more-button")

    JYOTICHAUHAN = (By.XPATH, '/html/body/div[1]/section[3]/div/a[1]') #href="https://www.updateland.com/save-instagram-photos-pc/"
    HASSEBAHMAD = (By.XPATH, '/html/body/div[1]/section[3]/div/a[2]') #href="https://twitgoo.com/grow-instagram-account-organically/"
    EDUARDOMORALES = (By.XPATH, '/html/body/div[1]/section[3]/div/a[3]') #href="https://hackernoon.com/the-best-instagram-bot-that-will-keep-your-account-safe-4aaf0ccaee4d"
    SNIGDHA = (By.XPATH, '/html/body/div[1]/section[3]/div/a[4]') #href="https://www.techpout.com/combin-scheduler-review/"
    CANBERKARINCI = (By.XPATH, '/html/body/div[1]/section[3]/div/a[5]') #href="https://digitalagencynetwork.com/how-to-schedule-instagram-posts-and-stories/"
    PARAMPREETCHANANA = (By.XPATH, '/html/body/div[1]/section[3]/div/a[6]') #href="https://www.reviewsxp.com/blog/combin-review/"
    JOHNPAULAGUIAR = (By.XPATH, '/html/body/div[1]/section[3]/div/a[7]') #href="https://www.johnpaulaguiar.com/combin-review-instagram-marketing-tool/"
    SHANEBARKER = (By.XPATH, '/html/body/div[1]/section[3]/div/a[8]') #href="https://shanebarker.com/blog/instagram-marketing-tools/"