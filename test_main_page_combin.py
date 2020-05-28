from pages.product.product_main_page_combin import ProductCombinMainPage
from pages.product.product_main_page_combin import ProductCombinMainPageLink

class TestCombinMainPage():

    def test_checking_text_and_pictures(self, browser):

        product_page = ProductCombinMainPage(browser, 'https://www.combin.com/')
        product_page.open()
        product_page.cookies_close()
        # FIRST CARDS
        product_page.product_headline()
        product_page.card_growth()
        product_page.card_growth_content()
        product_page.card_growth_logo()
        product_page.card_scheduler()
        product_page.card_scheduler_content()
        product_page.card_scheduler_logo()
        product_page.avialable()
        product_page.home_heading()
        # CARDS PRODUCTS
        product_page.card_attract_title()
        product_page.card_attract_text()
        product_page.card_attract_img()
        product_page.card_plan_sheduler_title()
        product_page.card_plan_scheduler_text()
        product_page.card_plan_scheduler_img()
        product_page.card_manage_title()
        product_page.card_manage_text()
        product_page.card_manage_img()
        product_page.card_communicate_title()
        product_page.card_communicate_text()
        product_page.card_communicate_img()
        product_page.card_track_title()
        product_page.card_track_text()
        product_page.card_track_img()
        # INFO CONTENT
        product_page.info_title()
        product_page.numeriqus()
        product_page.sej()
        product_page.forbes()
        product_page.product_hunt()
        # FEEDBACK
        product_page.brittney_feedback()
        product_page.brittney_instagram()
        product_page.brittney_user_name()
        product_page.brittney_img()
        product_page.now_for_free()
        # CARD PRODUCT
        product_page.card_growth_rounded()
        product_page.card_growth_background_logo()
        product_page.card_growth_background_heading()
        product_page.card_growth_background_img()
        product_page.card_scheduler_rounded()
        product_page.card_scheduler_background_heading()
        product_page.card_scheduler_background_logo()
        product_page.card_scheduler_background_img()
        product_page.our_latest_new_show_me()
        # BLOG
        product_page.blog_combin_left_card()
        product_page.blog_combin_left_card_img()
        product_page.blog_combin_left_card_text()
        product_page.blog_combin_medium_card()
        product_page.blog_combin_medium_card_img()
        product_page.blog_combin_medium_card_text()
        product_page.blog_combin_right_card()
        product_page.blog_combin_right_card_img()
        product_page.blog_combin_right_card_text()

    # Открытие ссылок ПЕРВЫХ КАРТОЧЕК на ГЛАВНОЙ странице КОМБИН
    def test_click_growth_card(self, browser):

        product_page = ProductCombinMainPageLink(browser, 'https://www.combin.com/')
        product_page.open()
        product_page.cookies_close()
        product_page.card_growth_button_try_for_free()
        product_page.download_block_growth_logo()
        product_page.download_block_growth_text()
        product_page.download_block_growth_input()
        product_page.download_block_try_for_free()
        product_page.card_growth_button_learn_more()
        product_page.current_url_growth()

    def test_click_scheduler_card(self, browser):

        product_page = ProductCombinMainPageLink(browser, 'https://www.combin.com/')
        product_page.open()
        product_page.cookies_close()
        product_page.card_scheduler_button_try_for_free()
        product_page.download_block_scheduler_logo()
        product_page.download_block_scheduler_text()
        product_page.download_block_scheduler_input()
        product_page.download_block_scheduler_try_for_free()
        product_page.card_scheduler_button_learn_more()
        product_page.current_url_scheduler()

    def test_check_links_growth_and_scheduler(self, browser):

        product_page = ProductCombinMainPageLink(browser, 'https://www.combin.com/')
        product_page.open()
        product_page.cookies_close()
        product_page.card_instagram_growth()
        product_page.card_free_instagram_scheduler()
        product_page.card_instagram_growth_manage()
        product_page.card_instagram_growth_communicate()
        product_page.card_instagram_growth_track()
        product_page.press()
        product_page.feedback_button_right()
        product_page.feedback_button_right2()
        product_page.feedback_instagram_id()

# rounded-block try-now__item combin and scheduler
    def test_check_last_download_block_growth_and_scheduler(self, browser):

        product_page = ProductCombinMainPageLink(browser, 'https://www.combin.com/')
        product_page.open()
        product_page.cookies_close()

        product_page.last_download_block_growth_learn_more()
        product_page.last_download_block_scheduler_learn_more()

        product_page.last_download_block_growth_try_for_free()
        product_page.last_download_block_growth_input()
        product_page.last_download_block_growth_try_free()

        product_page.last_download_block_scheduler_try_for_free()
        product_page.last_download_block_scheduler_input()
        product_page.last_download_block_scheduler_try_free()