from selenium.webdriver.common.by import By

class SchedulerPageLocators:
#Локаторы со страницы шедулера

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")
    AHEAD = (By.ID, "0")
    AUTOMATEDPUBLISHING = (By.ID, "1")
    IMAGESIZE = (By.ID, "2")
    LOCATIONTAGGING = (By.ID, "3")
    HASHTAGSACCOUNTSMENTIONING = (By.ID, "4")
    BULKSTORIES = (By.ID, "5")
    IMGCAROUSEL = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/scheduling-ahead.70b16bb87b3d.png"]')

    IMGSAVETIMEFLEXIBLE = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/save-time.ef11ed40cba4.png"]')
    HEADINGSAVETIMEPOSTSSCHEDULING = (By.XPATH, '/html/body/div[1]/section[4]/div/div/h3')
    TEXTSAVETIMEPOSTSSHEDULING = (By.XPATH, '/html/body/div[1]/section[4]/div/div/p')

    IMGCREATEDOZENS = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/create-dozens.5f2157cf983e.png"]')
    HEADINGCREATEDOZENS = (By.XPATH, '/html/body/div[1]/section[5]/div/div/h3')
    TEXTCREATEDOZENS = (By.XPATH, '/html/body/div[1]/section[5]/div/div/p')

    IMGSTYLEINSTAGRAMGRIL = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/style-layout.0046391f095e.png"]')
    HEADINGSTYLEINSTAGRAMGRIL = (By.XPATH, '/html/body/div[1]/section[6]/div/div/h3')
    TEXTSTYLEINSTAGRAMGRIL = (By.XPATH, '/html/body/div[1]/section[6]/div/div/p')

    IMGMANAGEGROWAUDIENCE = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/growth-promo.d4acd9a20352.png"]')
    HEADINGMANAGEGROWAUDIENCE = (By.XPATH, '/html/body/div[1]/section[9]/div/div/h3')
    LINKMANAGEGROWAUDIENCE = (By.CSS_SELECTOR, ".news__text-element.link-with-arrow.link-with-arrow--primary-color")

    EMAILFORSTARTPROMOSCHEDULER = (By.XPATH, '//*[@id="reminder-modal-scheduler"]/div/div[2]/form/div/input[1]')
    BUTTONTRYFREEPROMOSCHEDULER = (By.XPATH, '//*[@id="reminder-modal-scheduler"]/div/div[2]/form/div/button/span[2]')
    DOWNLOADBLOCKCLOSE = (By.XPATH, '//*[@id="reminder-modal-scheduler"]/a')
