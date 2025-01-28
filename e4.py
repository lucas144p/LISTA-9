import random

numero=random.randint(1, 100)

while True:
    chute = int(input("Adivinhe o número entre 1 e 100: "))
    if chute<numero:
        print('Muito baixo!\n')
    elif chute>numero:
        print('Muito alto!\n')
    else:
        print('Você acertou o número!')
        break