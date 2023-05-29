a,b = (int(x) for x in input("値をカンマで区切って入力:").split(","))

if a > b:
    big = a
    sma = b
else:
    big = b
    sma = a

while big % sma != 0:
    big_kari = sma
    sma = big % sma
    big = big_kari

print(sma)
