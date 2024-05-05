def mask_account_number(account_number: int) -> str:
    """Функция, которая принимает номер счета и выводит маскированный номер счета"""
    new_account_number = str(account_number)
    mask_account = "**" + new_account_number[-4:]
    return mask_account
