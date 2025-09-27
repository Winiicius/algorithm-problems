inicio, fim = list(map(int, input().split()))

horas = 0

if inicio == fim:
    horas = 24
elif inicio > fim:
    horas = 24 - inicio + fim
else:
    horas = fim - inicio

print(f"O JOGO DUROU {horas} HORA(S)")