# USANDO TRY EXCEPT
while(True):
    try:
        num = int(input())

        lista = list(map(int, input().split()))

        vel_max = max(lista)

        if vel_max < 10: print(1)
        elif vel_max < 20: print(2)
        else: print(3)
    except EOFError:
        break

# USANDO SYS
import sys

linhas = sys.stdin.readlines()  # lê todas as linhas de uma vez
i = 0

while i < len(linhas):
    num = int(linhas[i].strip())
    lista = list(map(int, linhas[i + 1].strip().split()))
    
    vel_max = max(lista)

    if vel_max < 10:
        print(1)
    elif vel_max < 20:
        print(2)
    else:
        print(3)

    i += 2  # avança duas linhas por vez


