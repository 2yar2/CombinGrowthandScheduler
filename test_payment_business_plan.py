from pages.product.product_payment_business_plan import PaymentBusinessPlan


class TestPaymentBusinessPlan():

    def test_payment_business(self, browser):

        product_page = PaymentBusinessPlan(browser, 'https://www.qa.combin.com/pricing/')
        product_page.open()
        product_page.cookies_close()
        product_page.button_business_subscribe_now()
        product_page.current_symbol_1()
        product_page.price_value_1()
        product_page.email()
        product_page.first_and_last_name()
        product_page.current_symbol_2()
        product_page.price_value_2()
        product_page.country()
        product_page.united_states()
        product_page.city()
        product_page.address()
        product_page.state()
        product_page.zip_code()
        product_page.name_on_card()
        #product_page.expiration_date()
        #product_page.card_cvc()
        product_page.card_number()


#    def test_payment_personal(self, browser):

#        product_page = PaymentPersonalPlan(browser, 'https://www.qa.combin.com/pricing/')
#        product_page.cookies_close()

