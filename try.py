import random

num = random.randint(1,30)
def game():
    n1 = int(input())
    if n1 == num:
        print('você ganhou!')
    if n1 < num:
        print(f"meu numero é maior que que {n1}. Tente novamente!")
        game()
    if n1 > num:
        print(f"meu numero é menor que {n1}. Tente novamente!")
        game()
print("o computador escolheu um numero de 1 a 30, tente descobrir-lo")
game()