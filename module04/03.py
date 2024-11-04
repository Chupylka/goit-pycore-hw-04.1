# знайти всі слова які написані з великої літери

#\b -> word boundaries (майже слово)
#r"\b[A-Z]+\b" - буде шукати слово
# ().() - крапка означатиме будь-який символ
# ().*() - * значатиме будь-який символ або текст (а може і не бути)

import re

text = "Theprice of PINEAPLLE ice cream is 20 uah"

# pattern = r"(\b[A-Z]+\b).*(\d{2}+)" ідентичні
# pattern = r"(\b[A-Z]+\b).*(\b\d+\b)"

pattern = r"(?P<word>\b[A-Z]+\b).*(?P<number>\b\d+\b)"

res = re.search(pattern, text)
print(res.groupdict()) #повертає словник
#print(res.groups())
#print(res.group(1)) # можна витягувати назву конкретної групи