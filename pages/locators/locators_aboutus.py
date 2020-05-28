from selenium.webdriver.common.by import By

class AboutUsPageLocators:

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")

    ABOUTUSHEADLINE = (By.CSS_SELECTOR, ".h1.about__headline")
    ABOUTUSTEXT = (By.CSS_SELECTOR, ".about__content .h2.about__text")

    CONTACTUSHEADLINE = (By.CSS_SELECTOR, ".h0.contact__headline")
    CONTACTUSTEXT = (By.CSS_SELECTOR, ".h2.contact__text.about__text")

    COMBINBLOG = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div/a[1]')
    COMBINTWITTER = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div/a[2]')
    COMBINYOUTUBE = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div/a[3]')
    COMBINREDDIT = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div/a[4]')

    SUPPORTTEAM = (By.XPATH, '/html/body/div[1]/section[2]/div[2]/div[1]/h3')
    SUPPORTTEAMEMAIL = (By.XPATH, '/html/body/div[1]/section[2]/div[2]/div[1]/a')

    MARKETINGTEAM = (By.XPATH, '/html/body/div[1]/section[2]/div[2]/div[2]/h3')
    MARKETINGTEAMEMAIL = (By.XPATH, '/html/body/div[1]/section[2]/div[2]/div[2]/a')

    DEVELOPMENTTEAM = (By.XPATH, '/html/body/div[1]/section[2]/div[2]/div[3]/h3')
    DEVELOPMENTTEAMEMAIL = (By.XPATH, '/html/body/div[1]/section[2]/div[2]/div[3]/a')

    EUROPEANOFFICE = (By.CSS_SELECTOR, ".address__wrapper.address__wrapper--european  .h3.address__heading.address__heading--left")
    EUROPEANADDRESSHEADING = (By.CSS_SELECTOR, ".address__wrapper.address__wrapper--european  .h3.address__heading.address__heading--local")
    EUROPEANADDRESSTEXT = (By.CSS_SELECTOR, ".address__wrapper.address__wrapper--european  .p.address__text")

    RUSSIANOFFICE = (By.CSS_SELECTOR, ".address__wrapper.address__wrapper--russian .h3.address__heading.address__heading--left")
    RUSSIANOFFICEADDRESSHEADING = (By.CSS_SELECTOR, ".address__wrapper.address__wrapper--russian .h3.address__heading.address__heading--local")
    RUSSIANOFFICEADDRESSTEXT = (By.CSS_SELECTOR, ".address__wrapper.address__wrapper--russian .p.address__text")

    DOWNLOADBLOCKLOGO = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div[1]')
    DOWNLOADBLOCKTEXT = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/h3[1]')
    DOWNLOADBLOCKINPUTEMAIL = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div[2]/form/div/input[1]')
    DOWNLOADBLOCKCHECKBOX = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div[2]/form/div/label/span')
    DOWNLOADBLOCKCHECKBOXTEXT = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div[2]/form/div/label/p')
    DOWNLOADBLOCKTRYFREE = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div[2]/form/div/button/span[2]')

    DOWNLOADBLOCKOPACITY = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div[2]/div[1]/p[1]')
    DOWNLOADBLOCKPRIVACYPOLICY = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div[2]/div[1]/p[1]/a')
    DOWNLOADBLOCKOS = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div[2]/div[1]/p[2]')
    DOWNLOADBLOCKAVALIABLE = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div[2]/div[2]')

