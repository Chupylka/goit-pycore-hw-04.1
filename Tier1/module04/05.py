# заміна слів на зірочки

import re


def replace(x):
    print(x)
    return "*" * len(x.group())

def replace_spam_words(text, spam_words):
    pattern = re.compile("|".join(spam_words))
    return re.sub(pattern, replace, text)

spam_words = ["idiot", "coder", "an", "to"]
text = "to be or not yo be an idiot. BE a good coder!"
moderated_text = replace_spam_words(text, spam_words)
print(moderated_text)

