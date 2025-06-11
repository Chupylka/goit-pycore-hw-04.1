#відфільтрувати 
# a.strip()-дозволяє підчистити всі пробіли з ліва та права
# a.lstrip()-дозволяє підчистити з ліва
# a.rstrip()-дозволяє підчистити з права
# sub - замінити

import re

def dad_filter(message):
    while ",," in message:
        message = message.replace(",,", ",")
    return message.strip(",")

def dad_filter_regex(message):
    return re.sub(",+", ",", message).strip(",")

res = dad_filter_regex("hsgdvhgdcg,,cdsc,dd,,,,,,,,,,,,,cdc,,,")
print(res)