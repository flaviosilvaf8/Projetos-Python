# Importando biblioteca random
import random

# Pontos do usuario e da maquina
user_points = 0 
computer_points = 0

options = ['r', 't', 'p']

while True:
    user_choice = input('Escolha R (Pedra) | T (Tesoura) | P (Papel) ou Q para sair: ').lower()

    # Caso o usuario escolha a letra 'q' sairá do laço de repetição
    if user_choice == 'q':
        break
    if user_choice not in options:
        continue
    
    computer_choice = random.randint(0, 2)
    # | 0: R | 1: T | 2: P
    computer_option = options[computer_choice]

    print(f'O computador escolheu: {computer_option}')

    # Lógica do jogo
    if user_choice == computer_option:
        print('Empate!')

    elif user_choice == 'r' and computer_option == 't':
        print('Você ganhou!')
        user_points = user_points + 1
    
    elif user_choice == 'p' and computer_option == 'r':
        print('Você ganhou!')
        user_points = user_points + 1

    elif user_choice == 't' and computer_option == 'p':
        print('Você ganhou!')
        user_points = user_points + 1
    
    else:
        print('Você perdeu!')
        computer_points = computer_points + 1


print(f'Sua pontuação {user_points}')
print(f'Pontuação do computador {computer_points}')

# Lógica da pontuação
if user_points == computer_points:
    print('Empate!')
elif user_points > computer_points:
    print('Parabéns! Você ganhou!')
else:
    print('Que pena! Você perdeu!')

print('Goodbye!')

    