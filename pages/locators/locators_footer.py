from selenium.webdriver.common.by import By

class LocatorsFooter():

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")

    ARIALABEL = (By.CSS_SELECTOR, ".footer__logo.background-image.combin-logo.combin-logo--text.combin-logo--primary")
    FOOTERCOPYRIGHT = (By.CSS_SELECTOR, ".footer__copyright")

    BLOGCOMBIN = (By.CSS_SELECTOR, ".community__item.community__item--medium")
    TWITTERCOMBIN = (By.CSS_SELECTOR, ".community__item.community__item--twitter")
    YOUTUBECOMBIN = (By.CSS_SELECTOR, ".community__item.community__item--youtube")
    REDDITCOMBIN = (By.CSS_SELECTOR, ".community__item.community__item--reddit")

#PRODUCT
    PRODUCT = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[2]/p')

    PRODUCTGROWTH = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[2]/a[1]')
    PRODUCTSCHEDULER = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[2]/a[2]')
    PRODUCTAIDAFORM = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[2]/a[3]')
    PRODUCTINSTACHECK = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[2]/a[4]')
    PRODUCTPRICING = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[2]/a[5]')
    PRODUCTDOWNLOAD = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[2]/a[6]')

#COMPANY

    COMPANY = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[3]/p')

    COMPANYABOUT = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[3]/a[1]')
    COMPANYBLOG = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[3]/a[2]')
    COMPANYROADMAP = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[3]/a[3]')
    COMPANYAFFILIATE = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[3]/a[4]')
    COMPANYPRESS = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[3]/a[5]')


#HELP

    HELP = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[4]/p')

    HELPGUIDES = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[4]/a[1]')
    HELPHOWTO = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[4]/a[2]')
    HELPFAQ = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[4]/a[3]')
    HELPTROUBLESHOOTING = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[4]/a[4]')

#USE CASES

    USECASES = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[5]/p')

    USECASESDETECTED = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[5]/a[1]')
    USECASESFIND = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[5]/a[2]')
    USECASESCHECK = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[5]/a[3]')
    USECASESSAVE = (By.XPATH, '/html/body/div[1]/footer/div[1]/div/nav[5]/a[4]')