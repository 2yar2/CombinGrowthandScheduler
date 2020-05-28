from pages.product.product_aboutus_page import ProductPageAboutUs


class TestAboutUsPage():

    def test_about_us(self, browser):
        product_page = ProductPageAboutUs(browser, 'https://www.combin.com/about/')
        product_page.open()

        product_page.about_us_headline()
        product_page.about_us_text()

        product_page.contact_us_heading()
        product_page.contact_us_text()

        product_page.combin_blog()
        product_page.combin_twitter()
        product_page.combin_youtube()
        product_page.combin_reddit()

        product_page.support_team()
        product_page.support_team_email()
        product_page.marketing_team_email()
        product_page.marketing_team()
        product_page.dev_team()
        product_page.dev_team_email()

        product_page.euro_office()
        product_page.euro_office_heading()
        product_page.euro_office_text()
        product_page.rus_office()
        product_page.rus_office_heading()
        product_page.rus_office_text()

        product_page.downloadblock_logo()
        product_page.downloadblock_text()
        product_page.downloadblock_email()
        product_page.download_checkbox()
        product_page.download_checbox_text()
        product_page.download_try_free()
        product_page.assept_alert()
        product_page.opacity()
        product_page.privacy_policy()
        product_page.os()
        product_page.avialable()