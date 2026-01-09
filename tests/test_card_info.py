from pages.card_page import CardPage


def test_card_information_is_visible(driver):
    card_page = CardPage(driver)

    assert card_page.is_card_number_visible(), "Card number is not visible"