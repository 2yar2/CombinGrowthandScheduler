from selenium.webdriver.common.by import By

class PaymentPlan():

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")

    BUTTONBUSINESSSUBSCRIBENOW = (By.XPATH, '//*[@id="subscribe-business-button"]')

    CURRENCYSYMBOL1 = (By.XPATH, '//*[@id="form-price-top"]/span[1]')
    PRICEVALUE1 = (By.XPATH, '//*[@id="form-price-top"]/span[2]')

    EMAIL = (By.ID, "payment-email")

    FIRSTANDLASTNAME = (By.XPATH, '//*[@id="payment-form"]/div[2]/div[2]/input')

    COUNTRY = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[1]/div[1]/div/div[2]/span/span')

    UNITEDSTATES = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[1]/div[1]/div/div[3]/div/ul/li[238]/a')

    CITY = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[1]/div[2]/input')

    ADDRESS = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[2]/input')

    STATE = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[3]/div[1]/input')

    ZIPCODE = (By.XPATH, '//*[@id="payment-form"]/div[3]/div[3]/div[2]/input')

    NAMEONCARD = (By.ID, "cardowner-field")

    CARDNUMBER = (By.CSS_SELECTOR, ".CardNumberField.CardNumberField--ltr")

    EXPIRATIONDATE = (By.XPATH, '//*[@id="card-expiry"]/div')

    CARDCVC = (By.XPATH, '//*[@id="card-cvc"]/div')

#TOTALPAYMENT

    CURRENCYSYMBOL2 = (By.XPATH, '//*[@id="form-price-bottom"]/span[1]')
    PRICEVALUE2 = (By.XPATH, '//*[@id="form-price-bottom"]/span[2]')

    SUBSCRIBE = (By.CSS_SELECTOR, ".button__text.subscription-card__button-text.payment-form__subscribe-button-text")
