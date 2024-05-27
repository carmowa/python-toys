#PROJETO DE JOGO DA FORCA
#GITHUB - CARMOWA

palavra= "natureza"
erros = 0
segredo = ""
letras_chutadas = ""

for i in palavra:
    if i == " ":
        segredo = segredo + "  " 
    else:
        segredo = segredo + "_ "

while erros<6 and '_' in segredo:
    print(f"{segredo}" + 
          f"\nerros: {erros}")
    letra = input("Insira uma LETRA: ")
    while len(letra)!=1 or not letra.isalpha():
        print("Este termo não respeita o campo, digite apenas uma LETRA.")
        letra = input("Insira uma LETRA: ")
    
    low_letra= letra.lower()
    letras_chutadas = letras_chutadas + low_letra
    
    if not low_letra in palavra:
        erros = erros + 1

    segredo = ""
    for i in palavra:
        if i in letras_chutadas:
            segredo = segredo + i + " "
        else:
            segredo = segredo + "_ "

if erros>=6:
    print(f"Você perdeu, a palavra era {palavra}!")
else:
    print(f"Você acertou, a palavra é {palavra}!")