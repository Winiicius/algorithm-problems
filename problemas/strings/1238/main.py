n = int(input())

palavras = []

for i in range(n):
    p = list(map(str, input().split()))

    maior = p[0] if len(p[0])>len(p[1]) else p[1]
    menor = p[0] if p[1] == maior else p[1]

    result = ""

    for i in range(len(menor)):
        result += p[0][i]
        result += p[1][i]
    
    if(len(maior) > len(menor)):
        result += maior[len(menor):]

    print(result)
