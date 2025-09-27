n = int(input())

lista = []
for i in range(n):
    num = int(input())
    lista.append(num)

dic = {}
for n in lista:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

ordenado = sorted(dic.items(), key=lambda item: (item[0]))

for v in ordenado:
    print(f"{v[0]} aparece {v[1]} vez(es)")