from src.widget import number_output


def mask_card_account_number(card_account_number: list) -> str:
    """Функция, которая принимает номер карты и номер счета выводит маскированный номер карты"""
    mask_number_account = ""
    for number in card_account_number:
        if len(number) == 16:
            mask_six_digits = number[7:12]
            stars = "** ****"
            mask_number_account += " " + number.replace(mask_six_digits, stars) + "\n"
        elif len(number) == 20:
            mask_number_account += " " + "**" + number[-4:] + "\n"
    return mask_number_account


# print(mask_card_account_number(number_output(['Maestro 1596837868705199',
#                                               'Счет 64686473678894779589',
#                                               'MasterCard 7158300734726758',
#                                               'Счет 35383033474447895560',
#                                               'Visa Classic 6831982476737658',
#                                               'Visa Platinum 8990922113665229',
#                                               'Visa Gold 5999414228426353',
#                                               'Счет 73654108430135874305'])))
