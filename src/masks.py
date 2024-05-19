def mask_card_account_number(card_account_number: list) -> str:
    """Функция, которая принимает номер карты и номер счета выводит маскированный номер карты"""
    mask_number_account = ""
    for number in card_account_number:
        if len(number) == 16:
            mask_six_digits = number[7:12]
            stars = "** ****"
            mask_number_account += " " + number.replace(mask_six_digits, stars)
        elif len(number) == 20:
            mask_number_account += " " + "**" + number[-4:]
    return mask_number_account
