def mask_card_number(card_number: int) -> str:
    """Функция, которая принимает номер карты и выводит маскированный номер карты"""
    new_number = str(card_number)
    mask_six_digits = new_number[7:12]
    stars = "** ****"
    mask_number = new_number.replace(mask_six_digits, stars)
    return mask_number


def mask_account_number(account_number: int) -> str:
    """Функция, которая принимает номер счета и выводит маскированный номер счета"""
    new_account_number = str(account_number)
    mask_account = "**" + new_account_number[-4:]
    return mask_account
