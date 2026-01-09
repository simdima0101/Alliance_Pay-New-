from pages.base_page import BasePage
from locators.card_locators import CardLocators


class CardPage(BasePage):

    def is_card_number_visible(self):
        return self.is_element_present(CardLocators.CARD_NUMBER)

    def get_balance(self):
        return self.find(CardLocators.BALANCE).text