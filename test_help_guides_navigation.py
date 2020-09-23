from pages.product.product_help_guides_navigation import ProductHelpGuidesNavigation

class TestHelpGuidesNavigation():

    def test_help_guides_navigation(self, browser):
        product_page = ProductHelpGuidesNavigation(browser, 'https://www.combin.com/guide/getting-started-to-grow-instagram-with-combin/')
        product_page.open()
        product_page.cookies_close()
        product_page.getting_started_to_grow_instagram_with_combin()
        product_page.getting_started_to_plan_instagram_publications_with_combin_scheduler()
        product_page.how_do_i_get_more_than_1000_search_results()
        product_page.what_are_combins_sorting_and_filtering_options_for_search_results()
        product_page.how_to_use_advanced_filters_and_machine_learning_analysis()
        product_page.how_to_add_instagram_accounts_to_combins_safe_list_in_batch()
        product_page.how_to_add_users_to_black_list_in_combin()
        product_page.how_to_backup_combin_user_lists_search_and_task_history()
        product_page.where_to_find_unfollowed_users_in_combin()
        product_page.how_to_export_users_lists_to_xls_csv()
        product_page.how_to_find_the_application_folder()
        product_page.how_to_login_to_account_registered_through_facebook()
        product_page.how_to_logout_without_losing_account_information()
        product_page.application_icons_and_their_meanings()
        product_page.application_keyboard_shortcuts()
        product_page.how_to_schedule_instagram_posts()
        product_page.how_to_schedule_instagram_stories()
