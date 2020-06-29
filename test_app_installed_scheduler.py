from pages.product.product_install_scheduler_page import AppInstalledScheduler


class TestInstalledSchedulerPage():

    def test_installed_scheduler_page(self, browser):

        product_page = AppInstalledScheduler(browser, 'https://www.combin.com/app-installed/?source=scheduler')
        product_page.open()
        product_page.cookies_close()
        product_page.installed_logo()
        product_page.installed_heading()
        product_page.installed_text()
        product_page.twitter_link()
        product_page.twitter_img()
        product_page.reddit_link()
        product_page.reddit_img()
        product_page.quora_link()
        product_page.quora_img()
        product_page.youtube_link()
        product_page.youtube_img()
        product_page.linkedin_link()
        product_page.linkedin_img()






