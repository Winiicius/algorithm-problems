n = int(input())

for i in range(n):
    pala = False
    lista = []
    frase = str(input())
    for l in frase:
        if l.isalpha():
            if pala == False:
                pala = True
                lista.append(l)
        else:
            pala = False
            continue
        continue
    print("".join(lista))

