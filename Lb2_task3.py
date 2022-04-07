def getRubles(num):
    group1 = [0, 5, 6, 7, 8, 9]
    group2 = [2, 3, 4]

    if (group1.count(num % 10) != 0 or num % 100 // 10 == 1):
        return f"{num} рублей"

    if (group2.count(num % 10) != 0):
        return f"{num} рубля"

    return f"{num} рубль"


for i in range(0, 40):
    print(getRubles(i))

print(getRubles(123))