import time 

t = input("Digite o tempo (em segundos): ")

if t.isdigit():
    t = int(t)
else:
    print("Entrada inválida!")
    quit()



while t != 0:
    minutes, seconds = divmod(t, 60) # função que retornará 2 numeros, o primeiro o quociente (minutes) e o resto da divisão (seconds)
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    print(timer, end="\r")
    time.sleep(1)
    t = t - 1

print("TEMPO ACABOU!")