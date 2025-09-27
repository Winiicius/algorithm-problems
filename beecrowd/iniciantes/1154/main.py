lista = []

while(True):
    n = int(input())
    if(n < 0):
        break;
    lista.append(n)

print(f"{sum(lista)/len(lista):.2f}")