from pages.product.product_download_page import ProductDownloadPage


class TestDownloadPage():

    def test_download_growth_win32(self, browser):
        product_page = ProductDownloadPage(browser, 'https://www.combin.com/download/')
        product_page.open()
        product_page.cookies_close()
        product_page.download_heading()
        product_page.switch_growth()
        product_page.product_logo_growth()
        product_page.version_element_growth()
        product_page.version_info()
        product_page.download_os_win32()
        product_page.icon_win32()
        product_page.text_win32()
        product_page.download_button_win32()
        product_page.release_date()
        product_page.system_requirments()


    def test_download_growth_win64(self, browser):
        product_page = ProductDownloadPage(browser, 'https://www.combin.com/download/')
        product_page.open()
        product_page.cookies_close()
        product_page.download_os_win64()
        product_page.icon_win64()
        product_page.text_win64()
        product_page.download_button_win64()


    def test_download_growth_macos(self, browser):
        product_page = ProductDownloadPage(browser, 'https://www.combin.com/download/')
        product_page.open()
        product_page.cookies_close()
        product_page.download_os_macos()
        product_page.icon_macos()
        product_page.text_macos()
        product_page.download_button_macos()


    def test_download_growth_ubuntu(self, browser):
        product_page = ProductDownloadPage(browser, 'https://www.combin.com/download/')
        product_page.open()
        product_page.cookies_close()
        product_page.download_os_ubuntu()
        product_page.icon_ubuntu()
        product_page.text_ubuntu()
        product_page.download_button_ubuntu()
        product_page.release_date()
        product_page.system_requirments()


#Scheduler

    def test_download_sheduler_win32(self, browser):
        product_page = ProductDownloadPage(browser, 'https://www.combin.com/download/')
        product_page.open()
        product_page.cookies_close()
        product_page.download_heading()
        product_page.switch_scheduler()
        product_page.product_logo_scheduler()
        product_page.version_element_scheduler()
        product_page.version_info()
        product_page.download_os_win32()
        product_page.icon_win32()
        product_page.text_win32()
        product_page.download_button_win32()
        product_page.release_date()
        product_page.system_requirments()


    def test_download_sheduler_win64(self, browser):
        product_page = ProductDownloadPage(browser, 'https://www.combin.com/download/')
        product_page.open()
        product_page.cookies_close()
        product_page.switch_scheduler()
        product_page.download_os_win64()
        product_page.icon_win64()
        product_page.text_win64()
        product_page.download_button_win64()


    def test_download_sheduler_macos(self, browser):
        product_page = ProductDownloadPage(browser, 'https://www.combin.com/download/')
        product_page.open()
        product_page.cookies_close()
        product_page.switch_scheduler()
        product_page.download_os_macos()
        product_page.icon_macos()
        product_page.text_macos()
        product_page.download_button_macos()


    def test_download_sheduler_ubuntu(self, browser):
        product_page = ProductDownloadPage(browser, 'https://www.combin.com/download/')
        product_page.open()
        product_page.cookies_close()
        product_page.switch_scheduler()
        product_page.download_os_ubuntu()
        product_page.icon_ubuntu()
        product_page.text_ubuntu()
        product_page.download_button_ubuntu()
        product_page.release_date()
        product_page.system_requirments()