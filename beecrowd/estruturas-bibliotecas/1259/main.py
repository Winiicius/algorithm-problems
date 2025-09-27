qtd_numeros = int(input())
pares = []
impares = []    

for i in range(qtd_numeros):
    numero = int(input())


    if ( numero % 2 == 0 ): pares.append(numero)
    else: impares.append(numero)

pares_ordenados:list = sorted(pares)
impares_ordenados = sorted(impares, reverse=True)

pares_ordenados.extend(impares_ordenados)

[print(i) for i in pares_ordenados]