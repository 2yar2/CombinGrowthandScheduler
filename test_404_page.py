from pages.product.product_404_page import Product404Page



class Test404Page():

    def test_404(self, browser):
        product_page = Product404Page(browser, 'https://www.combin.com/404')
        product_page.open()
        #product_page.cookies_close()
        product_page.page_not_found()
        product_page.error_text()
        product_page.error_link()