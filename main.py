import random

n = random.randrange(1, 50)
guess = int(input("Угадай чмсло от 1 до 50: "))
while n != guess:
    if guess < n:
        print("Загаданное число больше")
        guess = int(input("Следующая попытка: "))
    elif guess > n:
        print("Загаданное число меньше")
        guess = int(input("Следующая попытка: "))
    else:
        break
print("Ура Вы отгадали!")
