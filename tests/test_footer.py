from pages.product.product_footer import FooterOnMainPage


class TestFooterMain():

    def test_footer_main(self, browser):

        product_page = FooterOnMainPage(browser, 'https://www.combin.com/')
        product_page.open()
        product_page.cookies_close()
        product_page.aria_label()
        product_page.footer_copyright()
        product_page.blog_combin()
        product_page.twitter_combin()
        product_page.youtube_combin()
        product_page.reddit_combin()
        product_page.product()
        product_page.product_growth()
        product_page.product_aidaform()
        product_page.product_instacheck()
        product_page.product_scheduler()
        product_page.product_pricing()
        product_page.product_download()

        product_page.company()
        product_page.company_about()
        product_page.company_blog()
        product_page.company_press()
        product_page.company_affiliate()
        product_page.company_roadmap()

        product_page.help()
        product_page.help_faq()
        product_page.help_guides()
        product_page.help_how_to()
        product_page.help_troubleshooting()

        product_page.use_cases()
        product_page.use_cases_find()
        product_page.use_cases_save()
        product_page.use_cases_check()
        product_page.use_cases_detected()