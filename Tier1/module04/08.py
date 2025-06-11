# форматування 2
def formatted_numbers():
    res = list()
    header = "|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary")
    res.append(header)
    for i in range(16):
        res.append(f"|{i:=<10d}|{i:^10x}|{i:>10b}|")
    return res


for el in formatted_numbers():
    print(el)


# 110=> 6
# 2^2*2 + 2^1*1+2^0*0=4+2=6