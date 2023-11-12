#Jogo Da Forca
word = [] #Matriz Palavra Acertar
target = [] #Matriz de Acerto
verificar = [] #Matriz Letras Digitadas
life = 6 #Chances de Erros
repetir = 0 #Controle Repetição de Letras
cont0 = 0
cont1 = 0 #Contador Se Há Letra na Palavra
cont2 = 0 #Contador Letras Digitadas
keep = "1"
#print(word)
print("Soletre Uma Palavra")
print("Digite '0' Para Finalizar")
while keep != "0":
    letter = input().upper()
    word.append(letter)
    cont0 += 1
    keep = letter
print("Digite a Dica 1:")
tip1 = input().upper()
print("Digite a Dica 2:")
tip2 = input().upper()
print("Digite a Dica 3:")
tip3 = input().upper()
for x in range(0, 100, 1): #Criar Matriz Acerto
    print("")
print("Dica 1:")
print(tip1)
print("Você Tem", life, "Chances")
print("")
for x in range(0, cont0, 1): #Criar Matriz Acerto
    target.append("_")
print(target)
while life > 0:
    repetir = 0
    cont1 = 0
    print("Digite Uma Letra")
    letter = input().upper()
    for x in range(0, cont0, 1): #Adicionar Letra a Matriz Acerto
        if letter == word[x]:
            target[x] = letter
            cont1 += 1 #Ver se Tem a Letra na Palavra
    if cont2 > 0: 
        for y in range(0, cont2, 1): #Verifica se a Letra já Foi Digitada
            if verificar[y] == letter:
                repetir += 1
        if repetir == 0:
            verificar.append(letter) #Somente Adiciona Letra Diferente a Matriz Acerto
            cont2 +=1
    else: #Adiciona a Primeira Letra a Matriz Letras Digitadas
        verificar.append(letter)
        print(verificar)
        cont2 +=1
    if repetir > 0: #Letra Repetida Não Altera o Jogo
        print("Letra Já Digitada!")
        print("Não Perde Chance!")
        print("Continua Com", life, "Chances")
    else:
        if cont1 != 0: #Se Contador Vazio, Não Tem a Letra Digitada
            print("Acertou! A Palavra Tem Letra:", letter)
            print("Continua Com", life, "Chances")
        else:
            life -= 1
            print("Você Errou! A Palavra Não Tem Letra:", letter)
            print("Agora Tem", life, "Chances")
    print("Você Digitou a(s) Letra(s):", verificar)
    print("")
    print(target)
    if life == 3:
        print("Dica 2:")
        print(tip2)
    if life == 1:
        print("Dica 3:")
        print(tip3)
    if word == target:
        life = 0
if life == 0 and word == target:
    print("Parabéns! Você Ganhou!")
    print(":)")
else:
    print("")
    print("Você perdeu! Que Pena!")
    print("A Palavra Era:")
    print(word)
    print(":(")


    
