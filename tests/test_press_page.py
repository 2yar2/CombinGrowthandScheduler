from pages.product.product_press_page import ProductPress

class TestPressPage():

    def test_press_page(self, browser):

        product_page = ProductPress(browser, 'https://www.combin.com/press/')
        product_page.open()
        product_page.cookies_close()
# Block 1
        product_page.promo_title()
        product_page.promo_text()
        product_page.brand_assert()
        product_page.our_logo()
        product_page.our_logo_zip()
        product_page.our_text_1()
        product_page.press_download_logo_1()
        product_page.item_property_1()
        product_page.block_grey_logo_blue_1()
        product_page.block_blue_logo_white_1()
        product_page.our_symbol()
        product_page.our_symbol_zip()
        product_page.our_text_2()
        product_page.press_download_logo_2()
        product_page.item_property_2()
        product_page.block_grey_logo_blue_2()
        product_page.block_blue_logo_white_2()
# Press
        product_page.recent_press()
        product_page.viev_more()


# Block 2

    def test_press_page_block_2(self, browser):

        product_page = ProductPress(browser, 'https://www.combin.com/press/')
        product_page.open()
        product_page.cookies_close()
        product_page.screenshot_and_video()
        product_page.video_get_start()
        product_page.product_combin_screenshot()
        product_page.product_combin_screenshot_zip()
        product_page.download_media_kit()
        product_page.download_media_kit_pdf()