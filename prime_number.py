a =float(input("aの値を入力: "))

def prime(n):
    if n < 0:
        return print("負の値です")
    elif n.is_integer() == False:
        return print("少数です")

    limit = n ** (1/2)

    count = 2
    count2 = 0

    while count <= limit:
        if n % count == 0:
            count2 = 1
            break
        count += 1

    if count2 != 1:
        return print(str(n) + "は素数である")
    else: 
        return print(str(n) + "は素数でない")

prime(a)


