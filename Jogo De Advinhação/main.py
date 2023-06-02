import random

print("Seja bem vindo ao 'Adivinhe o número' do Flavio!")
choice_number = input("Digite o número teto do desafio: ") 

# Verifica se o caracter digitado é um numero
if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: valor informado não é numérico. Favor execute novamente e informe um número!")
    quit()

# Numero aleatório será entre 0 e o numero teto, setado pelo usuario
random_number = random.randint(0, choice_number)

n_choices = 0

while True:
    answer_user = input("Advinhe o número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: valor informado não é numérico. Favor informe um número!")
        continue #ignora tudo oque está abaixo e volta no While do loop
    
    n_choices = n_choices + 1 #somando numero de tentativas
    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("Chutou alto, o número randomico é menor que isso..")
    else:
        print("Chutou baixo, o número randomico é maior que isso..")

print("N° de tentativas: " + str(n_choices))