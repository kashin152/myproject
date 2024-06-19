from src.masks import mask_card_account_number


def test_mask_card_number():
    assert mask_card_account_number("1596837868705199") == " 1596837** ****5199"


def test_mask_account_number():
    assert mask_card_account_number("64686473678894779589") == " **9589"
