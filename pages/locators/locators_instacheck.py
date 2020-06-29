from selenium.webdriver.common.by import By

class LocatorsInstacheckPage:

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")

    PROMOINSTACHECKLOGO = (By.CSS_SELECTOR, ".product-promo__logo.background-image.instacheck-logo")

    INSTACHECKTITLE = (By.CSS_SELECTOR, ".h0.instacheck-section__title")
    INSTACHECKBUTTON = (By.CSS_SELECTOR, ".button-v2.instacheck__button")
    IMGINSTACHECKSECTION = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/instacheck/instacheck-promo.cc173041754c.png"]')

    SMALLLINEHEIGHTABOUTPRODUCTTEXT = (By.XPATH, '/html/body/div[1]/section[2]/div/div[1]/h2')

    GRABMOREENGAGEMENT = (By.XPATH, '/html/body/div[1]/section[2]/div/div[2]/div[1]/h3')
    USEEFFECTIVETACTICS = (By.XPATH, '/html/body/div[1]/section[2]/div/div[2]/div[1]/p')
    GRABMOREENGAGEMENTIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/instacheck/grab-engagement.070ddf89508e.png"]')

    CREATEBETTERCONTENT = (By.XPATH, '/html/body/div[1]/section[2]/div/div[2]/div[2]/h3')
    LEARNWHYYOURPOSTS = (By.XPATH, '/html/body/div[1]/section[2]/div/div[2]/div[2]/p')
    CREATEBETTERCONTENTIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/instacheck/create-content.cc6d1e617eb5.png"]')

    GETPERSONALGROWTH = (By.XPATH, '/html/body/div[1]/section[2]/div/div[2]/div[3]/h3')
    LEARNBESTTIPS = (By.XPATH, '/html/body/div[1]/section[2]/div/div[2]/div[3]/p')
    GETPERSONALGROWTHIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/instacheck/get-reccomendations.ee601a3fa3e7.png"]')

    FALLFORWARDSUCCESS = (By.XPATH, '/html/body/div[1]/section[2]/div/div[2]/div[4]/h3')
    ANALYZEYOURWEAKSPOTS = (By.XPATH, '/html/body/div[1]/section[2]/div/div[2]/div[4]/p')
    FALLFORWARDSUCCESSIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/instacheck/forward-success.2b87217d764a.png"]')

    GETBETTERWITHINSTACHECK = (By.CSS_SELECTOR, ".h0.h0--small-line-height.included-features__headline")
    GETBETTERWITHINSTACHECKIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/instacheck/total-profile-examination.60d270855b6c.png"]')
# Features
    TOTALPROFILE = (By.ID, "0")
    TOTALPROFILETEXT = (By.XPATH, '//*[@id="0"]/p')
    AESTHETICS = (By.ID, "1")
    AESTHETICSTEXT = (By.XPATH, '//*[@id="1"]/p')
    CONTENTCREATION = (By.ID, "2")
    CONTENTCREATIONTEXT = (By.XPATH, '//*[@id="2"]/p')
    CAPTIONANALYSIS = (By.ID, "3")
    CAPTIONANALYSISTEXT = (By.XPATH, '//*[@id="3"]/p')
    HASHTAGSANALYSIS = (By.ID, "4")
    HASHTAGSANALYSISTEXT = (By.XPATH, '//*[@id="4"]/p')
    ACCOUNTENGAGEMENT = (By.ID, "5")
    ACCOUNTENGAGEMENTTEXT = (By.XPATH, '//*[@id="5"]/p')

# About Product Instacheck

    INSTACHECKREPORTIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/instacheck/grow-and-flourish.e0ab245509b9.png"]')
    SMALLLINEHEIGHTINSTACHECKREPORTTEXT = (By.CSS_SELECTOR, ".h0.h0--small-line-height.about-product__text.instacheck-report__text")
    TEXTDARKINSTACHECKREPORTTEXT = (By.CSS_SELECTOR, ".text.text--dark.about-product__p.instacheck-report__text")

    INSTACHECKREPORTBUTTON = (By.CSS_SELECTOR, ".button-v2.instacheck-report__button")#href="https://static.combin.com/base/instacheck-report/InstaCheck-demo-report.572e452389df.pdf"
    INSTACHECKREPORTBUTTONARROW = (By.XPATH, '//img[@src="https://static.combin.com/base/img/icons/arrow-down-primary.6fa7748de21c.svg"]')

# FEEDBACK
    USERFEEDBACKTEXT1 = (By.XPATH, '/html/body/div[1]/section[5]/div/div/div/div/div[1]/div[1]/p')
    USERFEEDBACKNAME1 = (By.XPATH, '/html/body/div[1]/section[5]/div/div/div/div/div[1]/div[1]/span/p[1]')
    USERFEEDBACKPROF1 = (By.XPATH, '/html/body/div[1]/section[5]/div/div/div/div/div[1]/div[1]/span/p[2]')
    USERFEEDBACKIMG1 = (By.XPATH, '//img[@src="https://static.combin.com/base/img/users-photo/jaime-penzellna.2c61268e9aff.png"]')

    NEXTBUTTONFEEDBACKRIGHT = (By.XPATH, '/html/body/div[1]/section[5]/div/div/div/div/div[1]/div[2]/div[2]/div[2]')

    USERFEEDBACKTEXT2 = (By.XPATH, '/html/body/div[1]/section[5]/div/div/div/div/div[2]/div[1]/p')
    USERFEEDBACKNAME2 = (By.XPATH, '/html/body/div[1]/section[5]/div/div/div/div/div[2]/div[1]/span/p[1]')
    USERFEEDBACKPROF2 = (By.XPATH, '/html/body/div[1]/section[5]/div/div/div/div/div[2]/div[1]/span/p[2]')
    USERFEEDBACKIMG2 = (By.XPATH, '//img[@src="https://static.combin.com/base/img/users-photo/hamed-razzaghi.aa0951a6b337.png"]')

    NEXTBUTTONFEEDBACKLEFT = (By.XPATH, '/html/body/div[1]/section[5]/div/div/div/div/div[2]/div[2]/div[2]/div[1]')

    INSTACHECKGROW = (By.CSS_SELECTOR, ".h0.instacheck-grow__text.instacheck-report__text--center")

# CARDS Price
    CARD1 = (By.XPATH, '//*[@id="instacheck-prices"]/div/div[1]')
    CARD1PRICE = (By.XPATH, '//*[@id="instacheck-prices"]/div/div[1]/div[1]')
    CARD1HEADLINE = (By.XPATH, '//*[@id="instacheck-prices"]/div/div[1]/h3')
    CARD1MARGINBOT = (By.XPATH, '//*[@id="instacheck-prices"]/div/div[1]/p')
    CARD1BUTTONGETSTART = (By.XPATH, '//*[@id="instacheck-prices"]/div/div[1]/div[2]/div/a') #href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=M6G8ZCXZLBYX6"
    CARD1IMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/instacheck/personal-plan.b975fef13b3d.png"]')

    CARD2 = (By.XPATH, '//*[@id="instacheck-prices"]/div/div[2]')
    CARD2PRICE = (By.XPATH, '//*[@id="instacheck-prices"]/div/div[2]/div[1]')
    CARD2HEADLINE = (By.XPATH, '//*[@id="instacheck-prices"]/div/div[2]/h3')
    CARD2MARGINBOT = (By.XPATH, '//*[@id="instacheck-prices"]/div/div[2]/p')
    CARD2BUTTONGETSTART = (By.XPATH, '//*[@id="instacheck-prices"]/div/div[2]/div[2]/div/a') #href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=MMNEVK69SFZ6N"
    CARD2IMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/product-images/instacheck/business-plan.29578f9ec17e.png"]')

