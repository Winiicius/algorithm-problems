caso = 1
primeiro = True

while True:
    try:
        num = input()
        calc = input().split()
        d = {"F": 0, "M": 0}
        I = calc.count(num)

        if not primeiro:
            print()
        primeiro = False

        print(f"Caso {caso}:")
        print(f"Pares Iguais: {I}")

        for i, c in enumerate(calc):
            if c == "F" or c == "M":
                if calc[i - 1] == num:
                    d[c] += 1

        print(f"F: {d['F']}")
        print(f"M: {d['M']}")

        caso += 1

    except EOFError:
        break
