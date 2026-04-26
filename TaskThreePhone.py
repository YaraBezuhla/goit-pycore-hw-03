import re

def normalize_phone(phone_number):
    corect_number = []
    for number in phone_number:
        
        number_only_digits = re.sub(r"\D", "", number)
        if number_only_digits.startswith('380'):
            corect_number.append(f"+{number_only_digits}")
        else:
            corect_number.append(f"+38{number_only_digits}")


    print(corect_number)

numbers = input('Enter the numbers, separated by commas: ').split(",")
normalize_phone(numbers)