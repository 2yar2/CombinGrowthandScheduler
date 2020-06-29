from selenium.webdriver.common.by import By

class LocatorsDownloadPage:

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")

    DOWNLOADHEADING = (By.CSS_SELECTOR, ".h0.download__heading")

    #GROWTH
    SWITCHGROWTH = (By.CSS_SELECTOR, ".switch__option.switch__text.switch__text--first-option")
    PRODUCTLOGOGROWTH = (By.CSS_SELECTOR, ".download__product-logo.download__product-logo--growth")
    VERSIONELEMENTGROWTH = (By.CSS_SELECTOR, ".p.p--small.p--primary.download__text.download__text--version-info.download__text--version-info-growth")
    VERSIONINFO = (By.ID, "version-info")

    #SCHEDULER
    SWITCHSCHEDULER = (By.CSS_SELECTOR, ".switch__option.switch__text.switch__text--second-option")
    PRODUCTLOGOSCHEDULER = (By.CSS_SELECTOR, ".download__product-logo.download__product-logo--scheduler")
    VERSIONELEMENTSCHEDULER = (By.CSS_SELECTOR, ".p.p--small.p--primary.download__text.download__text--version-info.download__text--version-info-scheduler")

    # DOWNLOAD OS GROWTH AND SCHEDULER
    DOWNLOADOS = (By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/div/div[2]/span/span")

    ICONWIN32 = (By.XPATH, '/html/body/div[1]/section/div/div[1]/div[2]/div/div[3]/div/ul/li[1]/a/i') #HREF #windows-logo
    TEXTWIN32 = (By.XPATH, '/html/body/div[1]/section/div/div[1]/div[2]/div/div[3]/div/ul/li[1]/a/span')
    ICONWIN64 = (By.XPATH, '/html/body/div[1]/section/div/div[1]/div[2]/div/div[3]/div/ul/li[2]/a/i') #HREF #windows-logo
    TEXTWIN64 = (By.XPATH, '/html/body/div[1]/section/div/div[1]/div[2]/div/div[3]/div/ul/li[2]/a/span')
    ICONMACOS = (By.XPATH, '/html/body/div[1]/section/div/div[1]/div[2]/div/div[3]/div/ul/li[3]/a/i')#HREF #apple-logo
    TEXTMACOS = (By.XPATH, '/html/body/div[1]/section/div/div[1]/div[2]/div/div[3]/div/ul/li[3]/a/span')
    ICONUBUNTU = (By.XPATH, '/html/body/div[1]/section/div/div[1]/div[2]/div/div[3]/div/ul/li[4]/a/i') #HREF #ubuntu-logo
    TEXTUBUNTU = (By.XPATH, '/html/body/div[1]/section/div/div[1]/div[2]/div/div[3]/div/ul/li[4]/a/span')

    DOWNLOADBUTTON = (By.ID, "download-url")

    RELEASEDATE = (By.ID, "release-date")
    SYSTEMREQUIREMENTS = (By.CSS_SELECTOR, ".p.p--small.download__text.download__text--system-requirements") #ASSERT The application is supported on Windows 8 and newer, Mac OS 10.13 and newer, and Ubuntu 18.04 and newer (64-bit only).

