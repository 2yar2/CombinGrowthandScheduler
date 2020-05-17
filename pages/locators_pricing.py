from selenium.webdriver.common.by import By

class PricingLocators():
    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")
    PLANFOREVERYONE = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[1]/h1')
    SLIDERGROWTH = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[1]/label/span')

    STARTER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[1]/div[1]')
    STARTERHEADING = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/h2')
    STARTERGETSTARTED = (By.XPATH, '//*[@id="get-started-button"]/span')

    PERSONAL = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[2]/div[1]')
    PERSONALHEADING = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/h2')
    PERSONALPRICE = (By.ID, "subscription-price-personal")
    PERSONALSYMBOL = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/span/span[1]')
    PERSONALSUBSCRIBENOW = (By.XPATH, '//*[@id="subscribe-personal-button"]/span')

    BUSINESS = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[3]/div[1]')
    BUSINESSHEADING = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[3]/div[1]/h2')
    BUSINESSPRICE = (By.ID, "subscription-price-business")
    BUSINESSSYMBOL = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[3]/div[1]/span/span[1]')
    BUSINESSSUBSCRIBENOW = (By.XPATH, '//*[@id="subscribe-business-button"]/span')

    STARTERCARDFEATURES = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[1]/div[3]/ul[1]')
    PERSONALCARDFEATURES = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[2]/div[3]/ul[1]')
    BUSINESSCARDFEATURES = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[3]/div[3]/ul[1]')
    CURRENTLOCATION = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[2]/div[1]')
    ASKEDQUESTIONS = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/h1')

    HOWCANCANCELSUB = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[1]/div[1]')
    HOWCANCANCELSUBANSWER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[1]/div[2]/span/p')
    HOWCANCANCELTLIST = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[1]/div[2]/span/ul')
    HOWCANCANCELTLINK = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[1]/div[2]/span/ul/li[1]/p/a')

    PERSONALTOBUSINESS = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[2]/div[1]/h2')
    PERSONALTOBUSINESSANSWER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[2]/div[2]/span/p')
    PERSONALTOBUSINESSLIST = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[2]/div[2]/span/ul')
    PERSONALTOBUSINESSLINK = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[2]/div[2]/span/ul/li[1]/p/a')

    BUSINESSTOPERSONAL = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[3]/div/h2')
    BUSINESSTOPERSONALANSWER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[3]/span/div/p')
    BUSINESSTOPERSONALLINKCANCEL = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[3]/span/div/p/a[1]')
    BUSINESSTOPERSONALLINKSUB = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[3]/span/div/p/a[2]')

    RECEIVETHEKEY = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[4]/div/h2')
    RECEIVETHEKEYANSWER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[4]/span/div/p')
    RECEIVETHEKEYLIST = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[4]/span/div/ul')
    RECEIVETHEKEYLINK = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[4]/span/div/ul/li[1]/p/a')

    CANIUSEONELICENSE = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[5]/div/h2')
    CANIUSEONELICENSEANSWER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[5]/span/div')

    REFUNDPOLICY = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[6]/div/h2')
    REFUNDPOLICYANSWER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[6]/span/div/p')
    REFUNDPOLICYLINK = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[6]/span/div/p/a')

    SUBPAYMENT = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[7]/div/h2')
    SUBPAYMENTANSWER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[7]/span/div')
    SUBPAYMENTLINK = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[7]/span/div/p[2]/a')

    STARTERPLANFREE = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[8]/div/h2')
    STARTERPLANFREEANSWER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[8]/span/div')

    UPDATEBILLING = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[9]/div/h2')
    UPDATEBILLINGANSWER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[9]/span/div')
    UPDATEBILLINGLINK = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[3]/div/div/article[9]/span/div/p[2]/a')

    CONTACTUS = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/section/div[1]/h1')
    CONTACTUSTEXT = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/section/div[1]/p')

    COMBINBLOG = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/section/div[1]/div/a[1]')
    COMBINTWITTER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/section/div[1]/div/a[2]')
    COMBINYOUTUBE = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/section/div[1]/div/a[3]')
    COMBINREDDIT = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/section/div[1]/div/a[4]')

    SUPPORTTEAM = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/section/div[2]/div[1]/h3')
    SUPPORTTEAMEMAIL = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/section/div[2]/div[1]/a')

    MARKETINGTEAM = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/section/div[2]/div[2]/h3')
    MARKETINGTEAMEMAIL = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/section/div[2]/div[2]/a')

    DEVELOPMENTTEAM = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/section/div[2]/div[3]/h3')
    DEVELOPMENTTEAMEMAIL = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/section/div[2]/div[3]/a')

    SLIDERSCHEDULER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[1]/label/span/div[2]/p')

    STARTERSCHEDULER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[1]/div[3]/ul[2]')
    PERSONALSCHEDULER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[2]/div[3]/ul[2]')
    BUSINESSSCHEDULER = (By.XPATH, '//*[@id="initial-state"]/section/div/div/div[1]/div[2]/div[1]/div[3]/div[3]/ul[2]')