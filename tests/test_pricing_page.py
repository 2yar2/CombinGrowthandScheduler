from pages.product.product_pricing_page import ProductPagePricing
from pages.product.product_pricing_page import PricingScheduler
from pages.product.product_pricing_page import ContactUs

class TestPricingPage():

    def test_growth(self, browser):
        product_page = ProductPagePricing(browser, 'https://www.combin.com/pricing/')
        product_page.open()
        product_page.cookies_close()
        product_page.plan_for_every_one()
        product_page.slider_growth()
        product_page.starter_plan()
        product_page.starter_heading()
        product_page.starter_get_starter()
        product_page.starter_features()
        product_page.personal()
        product_page.personal_heading()
        product_page.personal_price()
        product_page.personal_symbol()
        product_page.personal_subscribe()
        product_page.personal_features()
        product_page.business_plan()
        product_page.business_heading()
        product_page.business_price()
        product_page.business_symbol()
        product_page.business_subscribe()
        product_page.business_feature()
        product_page.current_location()
        product_page.asked_question()
        product_page.cancel_subscribe()
        product_page.cancel_subscribe_answer()
        product_page.cancel_subscribe_list()
        product_page.cancel_subscribe_link()
        product_page.personal_to_business()
        product_page.personal_to_business_answer()
        product_page.personal_to_business_list()
        product_page.personal_to_business_link()
        product_page.business_to_personal()
        product_page.business_to_personal_answer()
        product_page.business_to_personal_link_cancel()
        product_page.business_to_personal_link_sub()
        product_page.receive_the_key()
        product_page.receive_the_key_answer()
        product_page.receive_the_key_list()
        product_page.receive_the_key_link()
        product_page.can_us_license()
        product_page.can_us_license_answer()
        product_page.refund_policy()
        product_page.refund_policy_answer()
        product_page.refund_policy_link()
        product_page.sub_payment()
        product_page.sub_payment_answer()
        product_page.sub_payment_link()
        product_page.starter_plan_free()
        product_page.starter_plan_free_answer()
        product_page.update_billing()
        product_page.update_billing_answer()
        product_page.update_billing_link()


    def test_contact_us(self, browser):
        product_page = ContactUs(browser, 'https://www.combin.com/pricing/')
        product_page.open()
        product_page.cookies_close()
        product_page.contact_us()
        product_page.contact_us_text()
        product_page.combin_blog()
        product_page.combin_twitter()
        product_page.combin_youtube()
        product_page.combin_reddit()
        product_page.support_team()
        product_page.support_team_email()
        product_page.marketing_team()
        product_page.marketing_team_email()
        product_page.dev_team()
        product_page.dev_team_email()


    def test_scheduler(self, browser):
        product_page = PricingScheduler(browser, 'https://www.combin.com/pricing/')
        product_page.open()
        product_page.cookies_close()
        product_page.slider_scheduler()
        product_page.unlimited_scheduler()
        product_page.subscription_card_button()
        product_page.free_price()
        product_page.instagram_accounts()
        product_page.link_in_bio()
        product_page.user_tagging()
        product_page.slider_growth()

        print(" Autotest Pricing Page PASS")