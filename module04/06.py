import re

# ("dhfduh?") - ? - означає що остання літера може бути або ні
# WWW - world wide web
# . - спеціальний символ
# \. - крапка
# [\w+_] - підстаеовка під будь-який символ


text = ("The jbvkjfbkvjfkjvbkfdjvbkdjbvb is https://www.edu.goit The jbdckbsbhdvsdb is https://chatgpt.com"
    "The jhjuvhus https://mail.google.com The jhdufdsu https://www.facebook.com The jdhfdhhsh https://www.app.facebook.com")


# регулярний вираз для urls адрес
pattern = re.compile(r"https?://w{3}?\.[\w+_\.]+\w{2,5}")
urls = re.findall(pattern, text)
print(urls)