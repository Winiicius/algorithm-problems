primeiro = True

while True:
    try:
        frase = input()
        dic = {}

        for i in frase:
            if i in dic:
                continue
            else:
                dic[i] = frase.count(i)

        ordenado_por_valor = sorted(dic.items(), key=lambda item: (item[1], -ord(item[0])))

        if not primeiro:
            print()  # quebra de linha entre blocos (não antes do primeiro)
        primeiro = False

        for a in ordenado_por_valor:
            print(ord(a[0]), a[1])

    except EOFError:
        break
