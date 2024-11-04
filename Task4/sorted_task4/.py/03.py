import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r"[^\d]", "", phone_number.strip())
    if cleaned_number.startswith("0"):
       cleaned_number = "+38" + cleaned_number

    elif cleaned_number.startswith("380"):
        cleaned_number = "+" + cleaned_number

    else:
       cleaned_number = "38" + cleaned_number
    return cleaned_number


raw_numbers = [
    "    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Numbers for SMS sending:", sanitized_numbers)
