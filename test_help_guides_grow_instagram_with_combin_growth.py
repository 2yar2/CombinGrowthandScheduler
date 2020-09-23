from pages.product.product_help_guides_grow_instagram_with_combin_growth import ProductHelpGuidesInstagramwithCombinGrowth

class TestHelpGuidesNavigation():

# Assert LINK on page

    def test_help_guides_instagram_with_combin_growth_link(self, browser):
        product_page = ProductHelpGuidesInstagramwithCombinGrowth(browser, 'https://www.combin.com/guide/getting-started-to-grow-instagram-with-combin/')
        product_page.open()
        product_page.cookies_close()
        product_page.activity_limits()
        product_page.main_product()
        product_page.download_growth()
        product_page.does_not_store_or_share_password()
        product_page.following_followers_ratio()
        product_page.display_purposes()
        product_page.batch()
        product_page.export_csv_xls()
        product_page.backup()


# Assert IMG and VIDEO on page
    def test_help_guides_instagram_with_combin_growth_img(self, browser):
        product_page = ProductHelpGuidesInstagramwithCombinGrowth(browser, 'https://www.combin.com/guide/getting-started-to-grow-instagram-with-combin/')
        product_page.open()
        product_page.cookies_close()
        product_page.youtube_video()
        product_page.img_loggining()
        product_page.img_profile()
        product_page.img_activation()
        product_page.img_proxy_setup()
        product_page.img_search()
        product_page.img_search_by_hashtag()
        product_page.img_search_by_haschtag_2()
        product_page.img_location()
        product_page.img_location_2()
        product_page.img_location_and_hashtag()
        product_page.img_user_search()
        product_page.img_user_search_2()
        product_page.img_filtering()
        product_page.img_advanced_filter()
        product_page.img_activities()
        product_page.img_comment()
        product_page.img_audience_management()
        product_page.img_tasks()