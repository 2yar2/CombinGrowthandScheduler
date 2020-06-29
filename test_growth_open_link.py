from pages.product.product_open_link_growth_page import OpenLinkWithGrowthPage

class TestOpenPageLinkWithGrowth():

    def test_open_youtube(self, browser):

        product_page = OpenLinkWithGrowthPage(browser, 'https://www.combin.com/product/instagram-growth/')
        product_page.open()
        product_page.cookies_close()
        product_page.watch_a_demo_video()


    def test_open_link_learn_more(self, browser):

        product_page = OpenLinkWithGrowthPage(browser, 'https://www.combin.com/product/instagram-growth/')
        product_page.open()
        product_page.cookies_close()
        product_page.open_learn_more_growth_page()

        print(" Autotest Growth Open Link PASS")
