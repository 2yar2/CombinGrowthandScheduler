from pages.product.product_install_growth_page import AppInstalledGrowth
from pages.product.product_install_growth_page import HowItWorksGrowth


class TestInstalledGrowthPage():
    @pytest.mark.regression
    def test_installed_growth_page(self, browser):

        product_page = AppInstalledGrowth(browser, 'https://www.combin.com/app-installed/?source=combin')
        product_page.open()
        product_page.cookies_close()
# APP INSTALLED
        product_page.installed_logo()
        product_page.installed_heading()
        product_page.installed_text()
        product_page.twitter_link()
        product_page.twitter_img()
        product_page.reddit_link()
        product_page.reddit_img()
        product_page.quora_link()
        product_page.quora_img()
        product_page.youtube_link()
        product_page.youtube_img()
        product_page.linkedin_link()
        product_page.linkedin_img()

# HOW WORKS
class TestHowItWorksGrowthPage():
    @pytest.mark.regression
    def test_how_it_works_growth_page(self, browser):

        product_page = HowItWorksGrowth(browser, 'https://www.combin.com/app-installed/?source=combin')
        product_page.open()
        product_page.cookies_close()
        product_page.how_it_works_heading()
        product_page.open_search()
        product_page.img_second()
        product_page.arrow_button_down_1()
        product_page.start_searching()
        product_page.img_third()
        product_page.arrow_button_down_2()
        product_page.find_new_people()
        product_page.img_fourth()
        product_page.arrow_button_down_3()
        product_page.perform_mass()
        product_page.img_fifth()
        product_page.arrow_button_down_4()
        product_page.watch_uor_video()
        product_page.video_tutorial_preview()
        product_page.video_tutorial()
        product_page.close_video()
        product_page.arrow_button_up()
        product_page.arrow_button_up()
        product_page.arrow_button_up()
        product_page.arrow_button_up()

