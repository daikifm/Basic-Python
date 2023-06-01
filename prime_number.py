a = int(input("aの値を入力: "))

limit = a ** (1/2)

count = 2
count2 = 0

while count <= limit:
    if a % count == 0:
        print(str(a) + "は素数でない")
        count2 = 1
        break
    count += 1
if count2 != 1:
    print(str(a) + "は素数である")