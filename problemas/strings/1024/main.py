n:int = int(input())

def criptografar(texto:str):
    lista = []
    for l in texto:
        if l.isalpha():
            if l == " ":
                continue
            lista.append(chr(ord(l)+3))
        else: lista.append(l)

    texto = "".join(lista)
    texto = texto[::-1]
    lista = []
    resto = texto[int(len(texto)/2):]
    for l in resto:
        lista.append(chr(ord(l)-1))
    print(texto[:int(len(texto)/2)] + "".join(lista))

for i in range(n):
    texto = str(input())
    criptografar(texto)