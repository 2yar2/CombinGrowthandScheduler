from selenium.webdriver.common.by import By

class Locators404:

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")

    PAGENOTFOUND = (By.XPATH, '/html/body/section/div/div[2]/h1')

    ERRORPAGETEXT = (By.XPATH, '/html/body/section/div/div[2]/p')

    ERRORPAGELINK = (By.XPATH, '/html/body/section/div/div[2]/p/a') #https://www.combin.com/
