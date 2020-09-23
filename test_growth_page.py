from pages.product.product_growth_page import ProductPage
from pages.product.product_growth_page import ProductPromo


class TestUserWhatIsIncluded():

    def test_open_growth_page(self, browser):

        product_page = ProductPage(browser, 'https://www.combin.com/product/instagram-growth/')
        product_page.open()
        product_page.cookies_close()
        product_page.click_to_growth()
        product_page.click_to_advanced()
        product_page.click_to_gender()
        product_page.click_to_machine()
        product_page.click_to_audience()
        product_page.click_to_repetitive()
        product_page.click_to_multiple()
        product_page.img_performance_statistics()
        product_page.img_detect()
        product_page.text_feature_heading()
        product_page.text_feature_list()
        product_page.img_check_quality()
        product_page.text_feature_heading()
        product_page.text_feature_list()
        product_page.img_check_quality()
        product_page.img_find_target()
        product_page.img_instagram_influencers()
        product_page.img_manage_activity()
        product_page.img_scheduler_promo()
        product_page.other_logo_scheduler()
        product_page.users_feedback()
        product_page.users_name_feedback()
        #product_page.arrow_button_right()
        #product_page.arrow_button_left()
        product_page.users_trust_us()
        product_page.logo_numeriques()
        product_page.logo_sej()
        product_page.logo_forbes()
        product_page.logo_online_marketing()
        product_page.logo_product_hunt()
        product_page.link_read_all_publication()
        product_page.link_learn_more()
        product_page.link_news_learn_more()
        product_page.video_hevc()
        product_page.video_av01()
        product_page.video_avc1()
        product_page.play_video()



    def test_growth_download_block_wrapper(self, browser):

        product_page = ProductPromo(browser, 'https://www.combin.com/product/instagram-growth/')
        product_page.open()
        product_page.cookies_close()
        product_page.button_try_for_free_promo()
        product_page.download_block_wrapper()
        product_page.email_for_start_promo()
        product_page.button_try_free_promo()
        product_page.button_try_for_free_promo()
        product_page.assept_alert()
        product_page.close_promo_block()
        product_page.email_for_start()
        product_page.button_try_free()
        product_page.assept_alert()



        print(" Autotest Growth Page PASS")