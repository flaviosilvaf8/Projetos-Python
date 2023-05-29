#função para separar as linhas
def simbolo(a):
    for s in range(40):
        print(a, end='')

simbolo('*')
print("\nSeja muito bem vindo ao quiz do Flavio!") 
simbolo('*')

resposta_usuario = input("\nVocê quer iniciar o quiz: (S/N)")

if resposta_usuario != 'S':
    quit()

score = 0

# 1ª pergunta
simbolo('-')
print("\nComeçando...")
simbolo('=')
print("\nQuem descobriu o Brasil? \n [A] Cristovão Colombo \n [B] Pedro Álvares Cabral \n [C] D.Pedro 1º")
resposta1 = input("Resposta: ")

if resposta1 == "B":
    print("Certa resposta!")
    score = score + 1
else:
    print("Errou! Resposta correta é letra B, Pedro Álvares Cabral\n")

simbolo('=')

# 2ª pergunta
print("\nQual o nome do pintor famoso que produziu Mona Lisa? \n [A] Leonardo Da Vinci \n [B] Pablo Picasso \n [C] Michelangelo")
resposta2 = input("Resposta: ")

if resposta2 == "A":
    print("Certa resposta!")
    score = score + 1
else:
    print("Errou! Resposta correta é letra A, Leonardo Da Vinci\n")

simbolo('=')

# 3ª pergunta
print("\nQual é a capital do Brasil? \n [A] Rio de Janeiro \n [B] Goiania \n [C] Brasília")
resposta3 = input("Resposta: ")

if resposta3 == "C":
    print("Certa resposta!")
    score = score + 1
else:
    print("Errou! Resposta correta é letra C, Brasília\n")

simbolo('=')

print(f'\nQuiz acabou... Pontuação: {score}/3\n')

simbolo('*')

if score <2:
    print("\nXiiiii... você mostrou um nível amador de conhecimento")
else:
    print("\nParabéns!!! Você é uma pessoa muito inteligente!")
