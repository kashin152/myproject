

from src.masks import mask_card_account_number


def test_mask_card_account_number(account_number):
    assert (
        mask_card_account_number(account_number)
        == " 1596837** ****5199 **9589 7158300** ****6758 **5560 6831982** ****7658 "
           "8990922** ****5229 5999414** ****6353 **4305"
    )
