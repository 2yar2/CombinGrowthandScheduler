from pages.product.product_change_location_and_price import ChangeLocationAndPrice

class TestChangeLocation():

    def test_change_loc_and_price(self, browser):

        product_page = ChangeLocationAndPrice(browser, 'https://www.combin.com/pricing/')
        product_page.open()
        product_page.cookies_close()
        product_page.current_location()
        product_page.france()
        product_page.price_in_euro_personal_card()
        product_page.price_in_euro_business_card()
        product_page.current_location()
        product_page.united_states()
        product_page.price_in_dollar_personal_card()
        product_page.price_in_dollar_business_card()
        product_page.current_location()
        product_page.spain()
        product_page.price_in_euro_personal_card()
        product_page.price_in_euro_business_card()
