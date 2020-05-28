from pages.base_page import BasePage
from pages.locators.locators_main_page_combin import MainPageCombinLocators
import time

class ProductCombinMainPage(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*MainPageCombinLocators.COOKIES_CLOSE)
        close.click()

# FIRST CARDS
    def product_headline(self):
        self.browser.find_element(*MainPageCombinLocators.PRODUCTHEADLINE)



    def card_growth(self):
        self.browser.find_element(*MainPageCombinLocators.CARDGROWTH)

    def card_growth_content(self):
        self.browser.find_element(*MainPageCombinLocators.CARDGROWTHCONTENT)

    def card_growth_logo(self):
        self.browser.find_element(*MainPageCombinLocators.CARDGROWTHLOGO)



    def card_scheduler(self):
        self.browser.find_element(*MainPageCombinLocators.CARDSCHEDULER)

    def card_scheduler_content(self):
        self.browser.find_element(*MainPageCombinLocators.CARDSCHEDULERCONTENT)

    def card_scheduler_logo(self):
        self.browser.find_element(*MainPageCombinLocators.CARDSCHEDULERLOGO)



    def avialable(self):
        self.browser.find_element(*MainPageCombinLocators.AVIALABLE)

    def home_heading(self):
        self.browser.find_element(*MainPageCombinLocators.CANYOUDOWITHCOMBINHOMEHEADING)


# CARDS PRODUCTS

    def card_attract_title(self):
        self.browser.find_element(*MainPageCombinLocators.ATTRACTNEWINSTAGRAMFOLLOWERSTITLE)

    def card_attract_text(self):
        self.browser.find_element(*MainPageCombinLocators.ATTRACTNEWINSTAGRAMFOLLOWERSTEXT)

    def card_attract_img(self):
        self.browser.find_element(*MainPageCombinLocators.ATTRACTNEWINSTAGRAMFOLLOWERSIMG)

    def card_plan_sheduler_title(self):
        self.browser.find_element(*MainPageCombinLocators.PLANSCHEDULEINSTAGRAMCONTENTTITLE)

    def card_plan_scheduler_text(self):
        self.browser.find_element(*MainPageCombinLocators.PLANSCHEDULEINSTAGRAMCONTENTTEXT)

    def card_plan_scheduler_img(self):
        self.browser.find_element(*MainPageCombinLocators.PLANSCHEDULEINSTAGRAMCONTENTIMG)

    def card_manage_title(self):
        self.browser.find_element(*MainPageCombinLocators.MANAGEMULTIPLEACCOUNTSTITLE)

    def card_manage_text(self):
        self.browser.find_element(*MainPageCombinLocators.MANAGEMULTIPLEACCOUNTSTEXT)

    def card_manage_img(self):
        self.browser.find_element(*MainPageCombinLocators.MANAGEMULTIPLEACCOUNTSIMG)

    def card_communicate_title(self):
        self.browser.find_element(*MainPageCombinLocators.COMMUNICATEWHITYOURAUDIENCETITLE)

    def card_communicate_text(self):
        self.browser.find_element(*MainPageCombinLocators.COMMUNICATEWHITYOURAUDIENCETEXT)

    def card_communicate_img(self):
        self.browser.find_element(*MainPageCombinLocators.COMMUNICATEWHITYOURAUDIENCEIMG)

    def card_track_title(self):
        self.browser.find_element(*MainPageCombinLocators.TRACKACTIVITYANDGROWTHTITLE)

    def card_track_text(self):
        self.browser.find_element(*MainPageCombinLocators.TRACKACTIVITYANDGROWTHTEXT)

    def card_track_img(self):
        self.browser.find_element(*MainPageCombinLocators.TRACKACTIVITYANDGROWTHIMG)

# INFO CONTENT
    def info_title(self):
        self.browser.find_element(*MainPageCombinLocators.INFOTITLE)

    def numeriqus(self):
        self.browser.find_element(*MainPageCombinLocators.NUMERIQUES)

    def sej(self):
        self.browser.find_element(*MainPageCombinLocators.SEJ)

    def forbes(self):
        self.browser.find_element(*MainPageCombinLocators.FORBES)

    def online_marketing(self):
        self.browser.find_element(*MainPageCombinLocators.ONLINEMARKETING)

    def product_hunt(self):
        self.browser.find_element(*MainPageCombinLocators.PRODUCTHUNT)

# FEEDBACK
    def brittney_feedback(self):
        self.browser.find_element(*MainPageCombinLocators.BRITTNEYFEEDBACK)

    def brittney_instagram(self):
        href = self.browser.find_element(*MainPageCombinLocators.BRITTNEYINSTAGRAM).get_attribute("href")
        assert href == "https://www.instagram.com/brittney_jae_/"

    def brittney_user_name(self):
        self.browser.find_element(*MainPageCombinLocators.BRITTNEYUSERNAME)

    def brittney_img(self):
        self.browser.find_element(*MainPageCombinLocators.BRITTNEYIMG)

    def now_for_free(self):
        self.browser.find_element(*MainPageCombinLocators.NOWFORFREEHOMEHEADING)


# CARD PRODUCT

    def card_growth_rounded(self):
        self.browser.find_element(*MainPageCombinLocators.CARDGROWTHROUNDED)

    def card_growth_background_logo(self):
        self.browser.find_element(*MainPageCombinLocators.CARDGROWTHBACKGROUNDLOGO)

    def card_growth_background_heading(self):
        self.browser.find_element(*MainPageCombinLocators.CARDGROWTHBACKGROUNDHEADING)

    def card_growth_background_img(self):
        self.browser.find_element(*MainPageCombinLocators.CARDGROWTHBACKGROUNDIMG)

    def card_scheduler_rounded(self):
        self.browser.find_element(*MainPageCombinLocators.CARDSCHEDULERROUNDED)

    def card_scheduler_background_logo(self):
        self.browser.find_element(*MainPageCombinLocators.CARDSCHEDULERBACKGROUNDLOGO)

    def card_scheduler_background_heading(self):
        self.browser.find_element(*MainPageCombinLocators.CARDSCHEDULERBACKGROUNDHEADING)

    def card_scheduler_background_img(self):
        self.browser.find_element(*MainPageCombinLocators.CARDSCHEDULERBACKGROUNDIMG)

    def our_latest_new_show_me(self):
        self.browser.find_element(*MainPageCombinLocators.OURLATESTNEWSHOMEHEADING)

# BLOG

    def blog_combin_left_card(self):
        self.browser.find_element(*MainPageCombinLocators.BLOGCOMBINLEFTCARD)

    def blog_combin_left_card_img(self):
        self.browser.find_element(*MainPageCombinLocators.BLOGCOMBINLEFTCARDIMG)

    def blog_combin_left_card_text(self):
        self.browser.find_element(*MainPageCombinLocators.BLOGCOMBINLEFTCARDTEXT)

    def blog_combin_medium_card(self):
        self.browser.find_element(*MainPageCombinLocators.BLOGCOMBINMEDIUMCARD)

    def blog_combin_medium_card_img(self):
        self.browser.find_element(*MainPageCombinLocators.BLOGCOMBINMEDIUMCARDIMG)

    def blog_combin_medium_card_text(self):
        self.browser.find_element(*MainPageCombinLocators.BLOGCOMBINMEDIUMCARDTEXT)

    def blog_combin_right_card(self):
        self.browser.find_element(*MainPageCombinLocators.BLOGCOMBINRIGHTCARD)

    def blog_combin_right_card_img(self):
        self.browser.find_element(*MainPageCombinLocators.BLOGCOMBINRIGHTCARDIMG)

    def blog_combin_right_card_text(self):
        self.browser.find_element(*MainPageCombinLocators.BLOGCOMBINRIGHTCARDTEXT)


# Открытие ссылок ПЕРВЫХ КАРТОЧЕК на ГЛАВНОЙ странице КОМБИН

class ProductCombinMainPageLink(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*MainPageCombinLocators.COOKIES_CLOSE)
        close.click()
    # FIRST CARD GROWTH
    def card_growth_button_try_for_free(self):
        button = self.browser.find_element(*MainPageCombinLocators.CARDGROWTHBUTTONTRYFORFREE)
        button.click()

    def download_block_growth_logo(self):
        self.browser.find_element(*MainPageCombinLocators.DOWNLOADBLOCKGROWTHLOGO)

    def download_block_growth_text(self):
        self.browser.find_element(*MainPageCombinLocators.DOWNLOADBLOCKGROWTHTEXT)

    def download_block_growth_input(self):
        input = self.browser.find_element(*MainPageCombinLocators.DOWNLOADBLOCKGROWTHINPUT)
        input.send_keys("openmedia2020@mail.ru")

    def download_block_try_for_free(self):
        button = self.browser.find_element(*MainPageCombinLocators.DOWNLOADBLOCKGROWTHTRYFORFREE)
        button.click()
        time.sleep(2)

    def card_growth_button_learn_more(self):
        button = self.browser.find_element(*MainPageCombinLocators.CARDGROWTHBUTTONLEARNMORE)
        button.click()

    def current_url_growth(self):
        get_url = self.browser.current_url
        assert get_url == "https://www.combin.com/product/instagram-growth/"

    # FIRST CARD SCHEDULER
    def card_scheduler_button_try_for_free(self):
        button = self.browser.find_element(*MainPageCombinLocators.CARDSCHEDULERBUTTONTRYFORFREE)
        button.click()

    def download_block_scheduler_logo(self):
        self.browser.find_element(*MainPageCombinLocators.DOWNLOADBLOCKSCHEDULERLOGO)

    def download_block_scheduler_text(self):
        self.browser.find_element(*MainPageCombinLocators.DOWNLOADBLOCKSCHEDULERTEXT)

    def download_block_scheduler_input(self):
        input = self.browser.find_element(*MainPageCombinLocators.DOWNLOADBLOCKSCHEDULERINPUT)
        input.send_keys("openmedia2020@mail.ru")

    def download_block_scheduler_try_for_free(self):
        button = self.browser.find_element(*MainPageCombinLocators.DOWNLOADBLOCKSCHEDULERTRYFORFREE)
        button.click()
        time.sleep(2)

    def card_scheduler_button_learn_more(self):
        button = self.browser.find_element(*MainPageCombinLocators.CARDSCHEDULERBUTTONLEARNMORE)
        button.click()

    def current_url_scheduler(self):
        get_url = self.browser.current_url
        assert get_url == "https://www.combin.com/product/free-instagram-scheduler/"

# Открытие ссылок на ГЛАВНОЙ странице КОМБИН

    def card_instagram_growth(self):
        link = self.browser.find_element(*MainPageCombinLocators.CARDINSTAGRAMGROWTH).get_attribute("href")
        assert link == "https://www.combin.com/product/instagram-growth/"

    def card_free_instagram_scheduler(self):
        link = self.browser.find_element(*MainPageCombinLocators.CARDFREEINSTAGRAMSCHEDULER).get_attribute("href")
        assert link == "https://www.combin.com/product/free-instagram-scheduler/"

    def card_instagram_growth_manage(self):
        link = self.browser.find_element(*MainPageCombinLocators.CARDINSTAGRAMGROWTHMANAGE).get_attribute("href")
        assert link == "https://www.combin.com/product/instagram-growth/"

    def card_instagram_growth_communicate(self):
        link = self.browser.find_element(*MainPageCombinLocators.CARDINSTAGRAMGROWTHCOMMUNICATE).get_attribute("href")
        assert link == "https://www.combin.com/product/instagram-growth/"

    def card_instagram_growth_track(self):
        link = self.browser.find_element(*MainPageCombinLocators.CARDINSTAGRAMGROWTHTRACK).get_attribute("href")
        assert link == "https://www.combin.com/product/instagram-growth/"

# Press and feedback
    def press(self):
        link = self.browser.find_element(*MainPageCombinLocators.PRESS).get_attribute("href")
        assert link == "https://www.combin.com/press/"

    def feedback_button_right(self):
        button = self.browser.find_element(*MainPageCombinLocators.FEEDBACKBUTTONRIGHT)
        button.click() # 2 raza
        time.sleep(2)

    def feedback_button_right2(self):
        button = self.browser.find_element(*MainPageCombinLocators.FEEDBACKBUTTONRIGHT2)
        button.click()


    def feedback_instagram_id(self):
        link = self.browser.find_element(*MainPageCombinLocators.FEEDBACKINSTAGRAMID).get_attribute("href")
        assert link == "https://www.instagram.com/mboroshirt/"

# rounded-block try-now__item combin and scheduler
    def last_download_block_growth_learn_more(self):
        link = self.browser.find_element(*MainPageCombinLocators.LASTDOWNLOADBLOCKGROWTHLEARNMORE).get_attribute("href")
        assert link == "https://www.combin.com/product/instagram-growth/"

    def last_download_block_scheduler_learn_more(self):
        link = self.browser.find_element(*MainPageCombinLocators.LASTDOWNLOADBLOCKSCHEDULERLEARNMORE).get_attribute("href")
        assert link == "https://www.combin.com/product/free-instagram-scheduler/"

    def last_download_block_growth_try_for_free(self):
        button = self.browser.find_element(*MainPageCombinLocators.LASTDOWNLOADBLOCKGROWTHTRYFORFREE)
        button.click()

    def last_download_block_growth_input(self):
        input = self.browser.find_element(*MainPageCombinLocators.LASTDOWNLOADBLOCKGROWTHINPUT)
        input.send_keys("openmedia2020@mail.ru")

    def last_download_block_growth_try_free(self):
        button = self.browser.find_element(*MainPageCombinLocators.LASTDOWNLOADBLOCKGROWTHTRYFREE)
        button.click()
        time.sleep(2)

    def last_download_block_scheduler_try_for_free(self):
        button = self.browser.find_element(*MainPageCombinLocators.LASTDOWNLOADBLOCKSHEDULERTRYFORFREE)
        button.click()

    def last_download_block_scheduler_input(self):
        input = self.browser.find_element(*MainPageCombinLocators.LASTDOWNLOADBLOCKSCHEDULERINPUT)
        input.send_keys("openmedia2020@mail.ru")

    def last_download_block_scheduler_try_free(self):
        button = self.browser.find_element(*MainPageCombinLocators.LASTDOWNLOADBLOCKSHEDULERTRYFREE)
        button.click()