from selenium.webdriver.common.by import By

class LocatorsIntercom:

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")

    INTERCOMLAUNCHER = (By.XPATH, "/html/body/div[9]/div/div[1]")

    SENDUSAMESSAGE = (By.XPATH, '//*[@id="intercom-container"]/div/div/div[1]/div[3]/div/div/div[1]/div/div/div/div/div/div[2]/button')

    INPUTEMAIL = (By.XPATH, '/html/body/div/div/div/div[1]/div[3]/div/div[2]/div/input')

    WRITEYOURMESSAGE = (By.XPATH, '//*[@id="intercom-container"]/div/div/div[1]/div[3]/div/div[2]/div/textarea')

    SENDMESSAGE = (By.XPATH, '//*[@id="intercom-container"]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/button[2]')

    REPLIESEANSWER = (By.XPATH, '//*[@id="intercom-container"]/div/div/div[1]/div[3]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div')

    EMAILANSWER = (By.XPATH, '//*[@id="intercom-container"]/div/div/div[1]/div[3]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[3]/div[1]/div/div[1]/div')

    MOREDETAILSANSWER = (By.XPATH, '//*[@id="intercom-container"]/div/div/div[1]/div[3]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[4]/div[1]/div/div[1]/div')

    NAMEANSWER = (By.XPATH, '//*[@id="intercom-container"]/div/div/div[1]/div[3]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[5]/div[1]/div/div[2]/div/div/div[1]')

    INPUTNAME = (By.XPATH, '//*[@id="intercom-container"]/div/div/div[1]/div[3]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[5]/div[1]/div/div[2]/div/div/div[2]/div/div/input')

    SUBMEET = (By.XPATH, '//*[@id="intercom-container"]/div/div/div[1]/div[3]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[5]/div[1]/div/div[2]/div/div/div[2]/div/div/button')

    THANKSANSWER = (By.XPATH, '//*[@id="intercom-container"]/div/div/div[1]/div[3]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[6]/div[1]/div[2]/div[1]/div')