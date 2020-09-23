from selenium.webdriver.common.by import By

class LocationAndPrice():

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")

    CURRENTLOCATION = (By.CSS_SELECTOR, ".location-selector__selected.user-country")

    FRANCE = (By.CSS_SELECTOR, "[data-index='74']")

    UNITEDSTATES = (By.CSS_SELECTOR, "[data-index='237']")

    SPAIN = (By.CSS_SELECTOR, "[data-index='208']")

    PERSONALCARDSYMBOL = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/span/span[1]')

    BUSINESSCARDSYMBOL = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[3]/div[1]/span/span[1]')

