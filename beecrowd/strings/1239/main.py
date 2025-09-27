while(True):
    try:
        sub = False
        ast = False

        frase = str(input())

        lista = []
        for l in frase:
            if l == "_":
                if sub == False:
                    lista.append("<i>")
                    sub = True
                else:
                    lista.append("</i>")
                    sub = False
            elif l == "*":
                if ast == False:
                    lista.append("<b>")
                    ast = True
                else:
                    lista.append("</b>")
                    ast = False
            else:
                lista.append(l)
        print("".join(lista))

    except EOFError:
        break