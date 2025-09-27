while(True):
    hora_inicio, minutos_inicio, hora_fim, minutos_fim = list(map(int, input().split()))
    
    if hora_inicio ==  minutos_inicio == hora_fim == minutos_fim == 0:
        break

    horas = 0
    if hora_inicio > hora_fim: hora_fim+=24
    if hora_inicio == hora_fim:
        if minutos_inicio > minutos_fim:
            horas = 23
            minutos = 60 - minutos_inicio + minutos_fim
        else:
            horas = 0
            minutos = minutos_fim - minutos_inicio 

    elif hora_fim > hora_inicio: # hora fim > hora inicio
        horas = hora_fim - hora_inicio
        if minutos_inicio > minutos_fim: # signfica que a diferença é menor que 1 hora
            horas -= 1
            minutos = 60 - minutos_inicio + minutos_fim
        else:
            minutos = minutos_fim - minutos_inicio

    elif hora_inicio > hora_fim:
        horas = 24 - hora_inicio + hora_fim
        if minutos_inicio > minutos_fim: # signfica que a diferença é menor que 1 hora
            horas -= 1
            minutos = 60 - minutos_inicio + minutos_fim
        else:
            minutos = minutos_inicio - minutos_fim

    print(horas*60 + minutos)

# RESPOSTA IA :(

# while True:
#     h1, m1, h2, m2 = map(int, input().split())
#     if h1 == m1 == h2 == m2 == 0:
#         break

#     inicio = h1 * 60 + m1
#     fim = h2 * 60 + m2

#     if fim <= inicio:
#         fim += 24 * 60  # adicionar um dia em minutos

#     print(fim - inicio)

    

        