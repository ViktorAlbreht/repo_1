



from random import randint
countN = int(input("Введите число монеток: "))
tails = 0
eagle = 0
count = 0
for i in range(countN):
    x = randint(0, 1)
    if x == 0:
        eagle += 1
    else:
        tails += 1
    print(x)
if eagle >= tails:
    count = countN - eagle
else:
    count = countN - tails
print('Минимальное количество монет, которые нужно перевернуть:', count)