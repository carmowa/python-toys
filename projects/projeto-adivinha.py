#PROJETO DE JOGO DE ADIVINHA
#GITHUB - CARMOWA

import random

num = random.randint(1, 1000)

print("UM NÚMERO ENTRE 1 E 1000 FOI SORTEADO, TENTE ACERTA-LO!")

for i in range(1, 11):
    chute = str(input("Insira um número: "))
    while not chute.isnumeric() or int(chute)<1 or int(chute)>1000:
        print("Esse termo não respeita o padrão.")
        chute = str(input("Insira um número: "))

    if int(chute)<num:
        print("\nTente um número maior!" + 
              f"\nVocê tem mais {10-i} tentativas.")
    elif int(chute)>num:
        print("\nTente um número menor!" + 
              f"\nVocê tem mais {10-i} tentativas.")
    else:
        print(f"\nParabéns! O número era {num}, você acertou na {i}ª tentativa!")
        exit()

print(f"\nVocê perdeu! O número sorteado era {num}.")