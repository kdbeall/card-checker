

def check(card_number):
    card_length = len(card_number)
    if card_length < 8 or card_length > 19:
        return False
    sum = 0
    parity = card_length % 2
    for i, digit in enumerate([int(x) for x in card_number]):
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        sum += digit
    return sum % 10 == 0
