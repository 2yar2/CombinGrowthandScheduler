from pages.product.product_scheduler_page import ProductPageScheduler
from pages.product.product_scheduler_page import ProductPromoScheduler

class TestSchedulerPage():

    def test_scheduler_page(self, browser):
        product_page = ProductPageScheduler(browser, 'https://www.combin.com/product/free-instagram-scheduler/')
        product_page.open()
        product_page.cookies_close()
        product_page.ahead_posting()
        product_page.auto_publishing()
        product_page.imgsize()
        product_page.loc_tag()
        product_page.hashtag_accountmentioning()
        product_page.bulk_stories()
        product_page.img_carousel()
        product_page.img_save_time()
        product_page.heading_save_time()
        product_page.text_save_time()
        product_page.img_create_dozens()
        product_page.heading_create_dozens()
        product_page.text_create_dozens()
        product_page.img_style_instagram_grid()
        product_page.heading_style_instagram_grid()
        product_page.text_style_instagram_grid()
        product_page.img_manage_grow_audience()
        product_page.heading_manage_grow_audience()
        product_page.link_manage_grow_audience()

    def test_scheduler_download_block_wrapper(self, browser):
        product_page = ProductPromoScheduler(browser, 'https://www.combin.com/product/free-instagram-scheduler/')
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



        print(" Autotest Scheduler Page PASS")