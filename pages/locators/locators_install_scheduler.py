from selenium.webdriver.common.by import By

class InstallSchedulerLocators():

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")

    INSTALLEDLOGO = (By.CSS_SELECTOR, "div.app-installed__logo")

    INSTALLEDHEADING = (By.CSS_SELECTOR, ".app-installed__heading.h1")
    INSTALLEDTEXT = (By.CSS_SELECTOR, ".app-installed__text.h2")

    TWITTERLINK = (By.XPATH, '/html/body/div[1]/section/div/div[2]/div/a[1]')
    TWITTERIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/sl-circle-twitter.6f5078ce3a32.png"]')

    REDDITLINK = (By.XPATH, '/html/body/div[1]/section/div/div[2]/div/a[2]')
    REDDITIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/sl-circle-reddit.987e4e7ce6e9.png"]')

    QUORALINK = (By.XPATH, '/html/body/div[1]/section/div/div[2]/div/a[3]')
    QUORAIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/sl-circle-quora.8f4eebcf9892.png"]')

    YOUTUBELINK = (By.XPATH, '/html/body/div[1]/section/div/div[2]/div/a[4]')
    YOUTUBEIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/sl-circle-youtube.1d11a1dc06c1.png"]')

    LINKEDINLINK = (By.XPATH, '/html/body/div[1]/section/div/div[2]/div/a[5]')
    LINKEDINIMG = (By.XPATH, '//img[@src="https://static.combin.com/base/img/sl-circle-linkedin.5c51931557d0.png"]')

