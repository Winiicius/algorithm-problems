while True:
    qtd_perguntras, freq_necessaria_perguntas = map(int, input().split())
    
    if qtd_perguntras == freq_necessaria_perguntas == 0:
        break
    
    perguntas = list(map(int, input().split()))

    frequentes = []
    
    for pergunta in perguntas:
        if perguntas.count(pergunta) >= freq_necessaria_perguntas:
            if pergunta not in frequentes:
                frequentes.append(pergunta)
    
    print(len(frequentes))

