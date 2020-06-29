from pages.product.product_instacheck_page import ProductInstacheckPage


class TestInstacheckPage():

    def test_instacheck(self, browser):
        product_page = ProductInstacheckPage (browser, 'https://www.combin.com/instacheck/')
        product_page.open()
        product_page.cookies_close()

# CHECK Cards
        product_page.promo_instacheck_logo()
        product_page.instacheck_title()
        product_page.instacheck_button()
        product_page.img_instacheck_section()
        product_page.small_line_height_about_product_text()
        product_page.grab_more_engagement()
        product_page.grab_more_engagement_img()
        product_page.use_effective_tactics()
        product_page.create_better_content()
        product_page.create_better_content_img()
        product_page.learn_why_your_posts()
        product_page.get_personal_growth()
        product_page.get_personal_growth_img()
        product_page.learn_best_tips()
        product_page.fall_forward_success()
        product_page.fall_forward_success_img()
        product_page.analyze_your_weak_spots()
        product_page.get_better_with_instacheck()
        product_page.get_better_with_instacheck_img()
# Features
        product_page.total_profile()
        product_page.total_profile_text()
        product_page.aes_the_tics()
        product_page.aes_the_tics_text()
        product_page.content_creation()
        product_page.content_creation_text()
        product_page.caption_analysis()
        product_page.caption_analysis_text()
        product_page.hashtag_analysis()
        product_page.hashtag_analysis_text()
        product_page.account_engagement()
        product_page.account_engagement_text()

# About Product Instacheck

        product_page.instacheck_repot_img()
        product_page.small_line_height_instacheck_report_text()
        product_page.text_dark_instacheck_report()
        product_page.instacheck_report_button()
        product_page.instacheck_report_button_arrow()

# CARDS Price
        product_page.card_1()
        product_page.card_1_img()
        product_page.card_1_price()
        product_page.card_1_headline()
        product_page.card_1_margin_bot()
        product_page.card_1_button_get_start()

        product_page.card_2()
        product_page.card_2_img()
        product_page.card_2_price()
        product_page.card_2_headline()
        product_page.card_2_margin_bot()
        product_page.card_2_button_get_start()



# FEEDBACK

class TestInstacheckFeedbackPage():

    def test_instacheck_feedback(self, browser):
        product_page = ProductInstacheckPage (browser, 'https://www.combin.com/instacheck/')
        product_page.open()
        product_page.cookies_close()

        product_page.user_feedback_text_1()
        product_page.user_feedback_name_1()
        product_page.user_feedback_prof_1()
        product_page.user_feedback_img_1()
        product_page.next_button_feedback_rigth()

        product_page.user_feedback_text_2()
        product_page.user_feedback_name_2()
        product_page.user_feedback_prof_2()
        product_page.user_feedback_img_2()
        product_page.next_button_feedback_left()