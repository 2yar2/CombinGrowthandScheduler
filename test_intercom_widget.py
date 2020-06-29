from pages.product.product_intercom_page import ProductIntercom

# НЕ РАБОТАЕТ

#class TestIntercomWidget():

#    def test_intercom(self, browser):
        product_page = ProductIntercom(browser, 'https://www.combin.com/about/')
        product_page.open()
        product_page.cookies_close()

        product_page.intercom_launcher()
        product_page.send_us_a_message()
        product_page.input_email()
        product_page.write_your_message()
        product_page.send_message()
        product_page.replies_answer()
        product_page.email_answer()
        product_page.more_details()
        product_page.name_answer()
        product_page.input_name()
        product_page.submeet()
        product_page.thank_answer()