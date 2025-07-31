n = int(input())

for i in range(n):
    lista = []
    texto:str = str(input())
    num = int(input())
    for l in texto:
        a = ord(l)
        b = a - num
        if b < 65:
            b = 91-(65-b)
        
        c = chr(b)

        lista.append(c)
    print("".join(lista))
