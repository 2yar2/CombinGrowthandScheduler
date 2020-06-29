from pages.locators.locators_instacheck import LocatorsInstacheckPage
from pages.base_page import BasePage


class ProductInstacheckPage(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*LocatorsInstacheckPage.COOKIES_CLOSE)
        close.click()

    def promo_instacheck_logo(self):
        self.browser.find_element(*LocatorsInstacheckPage.PROMOINSTACHECKLOGO)

    def instacheck_title(self):
        self.browser.find_element(*LocatorsInstacheckPage.INSTACHECKTITLE)

    def instacheck_button(self):
        button = self.browser.find_element(*LocatorsInstacheckPage.INSTACHECKBUTTON).get_attribute("href")
        assert button == "https://www.combin.com/instacheck/#instacheck-prices"

    def img_instacheck_section(self):
        self.browser.find_element(*LocatorsInstacheckPage.IMGINSTACHECKSECTION)

    def small_line_height_about_product_text(self):
        self.browser.find_element(*LocatorsInstacheckPage.SMALLLINEHEIGHTABOUTPRODUCTTEXT)

    def grab_more_engagement(self):
        self.browser.find_element(*LocatorsInstacheckPage.GRABMOREENGAGEMENT)

    def use_effective_tactics(self):
        self.browser.find_element(*LocatorsInstacheckPage.USEEFFECTIVETACTICS)

    def grab_more_engagement_img(self):
        self.browser.find_element(*LocatorsInstacheckPage.GRABMOREENGAGEMENTIMG)

    def create_better_content(self):
        self.browser.find_element(*LocatorsInstacheckPage.CREATEBETTERCONTENT)

    def learn_why_your_posts(self):
        self.browser.find_element(*LocatorsInstacheckPage.LEARNWHYYOURPOSTS)

    def create_better_content_img(self):
        self.browser.find_element(*LocatorsInstacheckPage.CREATEBETTERCONTENTIMG)

    def get_personal_growth(self):
        self.browser.find_element(*LocatorsInstacheckPage.GETPERSONALGROWTH)

    def learn_best_tips(self):
        self.browser.find_element(*LocatorsInstacheckPage.LEARNBESTTIPS)

    def get_personal_growth_img(self):
        self.browser.find_element(*LocatorsInstacheckPage.GETPERSONALGROWTHIMG)

    def fall_forward_success(self):
        self.browser.find_element(*LocatorsInstacheckPage.FALLFORWARDSUCCESS)

    def analyze_your_weak_spots(self):
        self.browser.find_element(*LocatorsInstacheckPage.ANALYZEYOURWEAKSPOTS)

    def fall_forward_success_img(self):
        self.browser.find_element(*LocatorsInstacheckPage.FALLFORWARDSUCCESSIMG)

    def get_better_with_instacheck(self):
        self.browser.find_element(*LocatorsInstacheckPage.GETBETTERWITHINSTACHECK)

    def get_better_with_instacheck_img(self):
        self.browser.find_element(*LocatorsInstacheckPage.GETBETTERWITHINSTACHECKIMG)

#Features
    def total_profile(self):
        self.browser.find_element(*LocatorsInstacheckPage.TOTALPROFILE).click()

    def total_profile_text(self):
        self.browser.find_element(*LocatorsInstacheckPage.TOTALPROFILETEXT)

    def aes_the_tics(self):
        self.browser.find_element(*LocatorsInstacheckPage.AESTHETICS).click()

    def aes_the_tics_text(self):
        self.browser.find_element(*LocatorsInstacheckPage.AESTHETICSTEXT)

    def content_creation(self):
        self.browser.find_element(*LocatorsInstacheckPage.CONTENTCREATION).click()

    def content_creation_text(self):
        self.browser.find_element(*LocatorsInstacheckPage.CONTENTCREATIONTEXT)

    def caption_analysis(self):
        self.browser.find_element(*LocatorsInstacheckPage.CAPTIONANALYSIS).click()

    def caption_analysis_text(self):
        self.browser.find_element(*LocatorsInstacheckPage.CAPTIONANALYSISTEXT)

    def hashtag_analysis(self):
        self.browser.find_element(*LocatorsInstacheckPage.HASHTAGSANALYSIS).click()

    def hashtag_analysis_text(self):
        self.browser.find_element(*LocatorsInstacheckPage.HASHTAGSANALYSISTEXT)

    def account_engagement(self):
        self.browser.find_element(*LocatorsInstacheckPage.ACCOUNTENGAGEMENT).click()

    def account_engagement_text(self):
        self.browser.find_element(*LocatorsInstacheckPage.ACCOUNTENGAGEMENTTEXT)

# About Product Instacheck

    def instacheck_repot_img(self):
        self.browser.find_element(*LocatorsInstacheckPage.INSTACHECKREPORTIMG)

    def small_line_height_instacheck_report_text(self):
        self.browser.find_element(*LocatorsInstacheckPage.SMALLLINEHEIGHTINSTACHECKREPORTTEXT)

    def text_dark_instacheck_report(self):
        self.browser.find_element(*LocatorsInstacheckPage.TEXTDARKINSTACHECKREPORTTEXT)

    def instacheck_report_button(self):
        href = self.browser.find_element(*LocatorsInstacheckPage.INSTACHECKREPORTBUTTON).get_attribute("href")
        assert href == "https://static.combin.com/base/instacheck-report/InstaCheck-demo-report.572e452389df.pdf"

    def instacheck_report_button_arrow(self):
        self.browser.find_element(*LocatorsInstacheckPage.INSTACHECKREPORTBUTTONARROW)


# CARDS Price
#1
    def card_1(self):
        self.browser.find_element(*LocatorsInstacheckPage.CARD1)

    def card_1_price(self):
        self.browser.find_element(*LocatorsInstacheckPage.CARD1PRICE)

    def card_1_headline(self):
        self.browser.find_element(*LocatorsInstacheckPage.CARD1HEADLINE)

    def card_1_margin_bot(self):
        self.browser.find_element(*LocatorsInstacheckPage.CARD1MARGINBOT)

    def card_1_button_get_start(self):
        href = self.browser.find_element(*LocatorsInstacheckPage.CARD1BUTTONGETSTART).get_attribute("href")
        assert href == "https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=M6G8ZCXZLBYX6"

    def card_1_img(self):
        self.browser.find_element(*LocatorsInstacheckPage.CARD1IMG)

#2
    def card_2(self):
        self.browser.find_element(*LocatorsInstacheckPage.CARD2)

    def card_2_price(self):
        self.browser.find_element(*LocatorsInstacheckPage.CARD2PRICE)

    def card_2_headline(self):
        self.browser.find_element(*LocatorsInstacheckPage.CARD2HEADLINE)

    def card_2_margin_bot(self):
        self.browser.find_element(*LocatorsInstacheckPage.CARD2MARGINBOT)

    def card_2_button_get_start(self):
        href = self.browser.find_element(*LocatorsInstacheckPage.CARD2BUTTONGETSTART).get_attribute("href")
        assert href == "https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=MMNEVK69SFZ6N"

    def card_2_img(self):
        self.browser.find_element(*LocatorsInstacheckPage.CARD2IMG)

# FEEDBACK
#1
    def user_feedback_text_1(self):
        self.browser.find_element(*LocatorsInstacheckPage.USERFEEDBACKTEXT1)

    def user_feedback_name_1(self):
        self.browser.find_element(*LocatorsInstacheckPage.USERFEEDBACKNAME1)

    def user_feedback_prof_1(self):
        self.browser.find_element(*LocatorsInstacheckPage.USERFEEDBACKPROF1)

    def user_feedback_img_1(self):
        self.browser.find_element(*LocatorsInstacheckPage.USERFEEDBACKIMG1)

    def next_button_feedback_rigth(self):
        self.browser.find_element(*LocatorsInstacheckPage.NEXTBUTTONFEEDBACKRIGHT).click()

#2
    def user_feedback_text_2(self):
        self.browser.find_element(*LocatorsInstacheckPage.USERFEEDBACKTEXT2)

    def user_feedback_name_2(self):
        self.browser.find_element(*LocatorsInstacheckPage.USERFEEDBACKNAME2)

    def user_feedback_prof_2(self):
        self.browser.find_element(*LocatorsInstacheckPage.USERFEEDBACKPROF2)

    def user_feedback_img_2(self):
        self.browser.find_element(*LocatorsInstacheckPage.USERFEEDBACKIMG2)

    def next_button_feedback_left(self):
        self.browser.find_element(*LocatorsInstacheckPage.NEXTBUTTONFEEDBACKLEFT).click()

    def instacheck_grow(self):
        self.browser.find_element(*LocatorsInstacheckPage.INSTACHECKGROW)