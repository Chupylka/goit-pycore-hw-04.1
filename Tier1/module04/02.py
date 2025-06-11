# регулярні вирази які будуть шукати в рядку айпі адреси

import re


text = "Bot activity detected: 32.16.4.162, 69.168.21.343 looks suspicios"

pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
print(pattern)
ips = re.findall(pattern, text)

ips = re.sub(pattern, text)

ips = re.search(pattern, text)

print(ips)