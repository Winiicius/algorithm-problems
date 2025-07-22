# lista = list(map(int, input().split())) ## ERRADO POIS LÊ 10 NUMEROS NA MESMA LINHA SEPARADOS POR ESPAÇO
# for i, n in enumerate(lista):
#     print(f"X[{i}] = {n if n > 0 else 1}")

## CODIGO CORRETO, LÊ 10 NUMERO UM EM CADA LINHA

lista = []
for _ in range(10):
    n = int(input())
    lista.append(n if n > 0 else 1)

for i, n in enumerate(lista):
    print(f"X[{i}] = {n}")
