while True:
    try:
        n_dias = int(input())
        custoPorDia = int(input())

        lucros = []

        for i in range(n_dias):
            lucros.append(int(input()))

        
        max_ate_agora = 0
        max_termina_aqui = 0

        for j in lucros:
            max_termina_aqui = max(0, max_termina_aqui + j - custoPorDia)
            max_ate_agora = max(max_ate_agora, max_termina_aqui)
        print(max_ate_agora)

    except EOFError:
        break