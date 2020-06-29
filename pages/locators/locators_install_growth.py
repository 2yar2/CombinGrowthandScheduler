from selenium.webdriver.common.by import By

class InstallGrowthLocators():

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")
# APP INSTALLED
    INSTALLEDLOGO = (By.CSS_SELECTOR, "div.app-installed__logo")
    INSTALLEDHEADING = (By.CSS_SELECTOR, ".app-installed__heading.h1")
    INSTALLEDTEXT = (By.CSS_SELECTOR, ".app-installed__text.h2")

    TWITTERLINK = (By.XPATH, '/html/body/div[1]/section[1]/div/div[2]/div/a[1]')
    TWITTERIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/sl-circle-twitter.6f5078ce3a32.png"]')

    REDDITLINK = (By.XPATH, '/html/body/div[1]/section[1]/div/div[2]/div/a[2]')
    REDDITIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/sl-circle-reddit.987e4e7ce6e9.png"]')

    QUORALINK = (By.XPATH, '/html/body/div[1]/section[1]/div/div[2]/div/a[3]')
    QUORAIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/sl-circle-quora.8f4eebcf9892.png"]')

    YOUTUBELINK = (By.XPATH, '/html/body/div[1]/section[1]/div/div[2]/div/a[4]')
    YOUTUBEIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/sl-circle-youtube.1d11a1dc06c1.png"]')

    LINKEDINLINK = (By.XPATH, '/html/body/div[1]/section[1]/div/div[2]/div/a[5]')
    LINKEDINIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/sl-circle-linkedin.5c51931557d0.png"]')

# HOW WORKS

    HOWITWORKSHEADING = (By.CSS_SELECTOR, "h1.how-works__headline")
    OPENSEARCH = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div[1]/div[2]/div/div[1]/div/p')
    IMGSECOND = (By.XPATH, '/html/body/div[1]/section[2]/div[2]/div[2]/div/div/div[1]/div/div')
    ARROWBUTTONDOWN1 = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div[1]/div[3]')

    STARTSEARCHING = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div[1]/div[2]/div/div[2]/div/p')
    IMGTHIRD = (By.CSS_SELECTOR, ".carousel-picture__image.carousel-picture__image--third")
    ARROWBUTTONDOWN2 = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div[1]/div[3]')

    FINDNEWPEOPLE = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div[1]/div[2]/div/div[3]/div/p')
    IMGFOURTH = (By.CSS_SELECTOR, ".carousel-picture__image.carousel-picture__image--fourth")
    ARROWBUTTONDOWN3 = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div[1]/div[3]')

    PERFORMMASS = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div[1]/div[2]/div/div[4]/div/p')
    IMGFIFTH = (By.CSS_SELECTOR, ".carousel-picture__image.carousel-picture__image--fifth")
    ARROWBUTTONDOWN4 = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div[1]/div[3]')

    WATCHOURVIDEO = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div[1]/div[2]/div/div[5]/div/p') #HREF
    VIDEOTUTORIALPREVIEW = (By.CSS_SELECTOR, ".carousel-picture__image.carousel-picture__image--video-tutorial-preview")
    VIDEOTOTURIAL = (By.XPATH, '//iframe[@src="https://www.youtube.com/embed/mx7vra8DP0g?enablejsapi=1"]')

    CLOSEVIDEO = (By.XPATH, '/html/body/div[6]/div/a')

    ARROWBUTTONUP = (By.XPATH, '/html/body/div[1]/section[2]/div[1]/div[1]/div[1]')
