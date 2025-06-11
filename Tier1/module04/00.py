


import re


def find_max_vowels(text):
    sep = "|#"
    vowels = "aeiou"
    for char in text:
        if char.lower() not in vowels:
            text = text.replace(char, sep)

        chains = text.split(sep)
        chains.sort(reverse=True)
        max_vowels = chains[0]
        return max_vowels, len(max_vowels)
    
def find_max_vowels_reg(text):
    pattern = r"[aeiou]+"
    return max(re.findall(pattern, text, flags=re.IGNORECASE | re.DEBUG), key=len)


    
text = "aevjeaeaeakbdkjbsdjbv khjvjkeaeaesd cj 01kjeeeeeeeeeebfvgb"
res = find_max_vowels_reg(text)
print(res)
