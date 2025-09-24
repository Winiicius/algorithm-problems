
while True:

    qtdBancos, deb = map(int, input().split())

    if qtdBancos == deb == '0':
        break

    saldos = list(map(int, input().split()))

    for i in range(int(deb)):

        transacoes = list(map(int, input().split()))

        bancoDevedor = saldos[transacoes[0]-1]
        bancoCredor = saldos[transacoes[1]-1]

        bancoDevedor = bancoDevedor - transacoes[2]
        bancoCredor = bancoCredor + transacoes[2]

        saldos[transacoes[0]-1] = bancoDevedor
        saldos[transacoes[1]-1] = bancoCredor

    negativo = False

    for i in saldos:
        if i < 0:
            print('N')
            negativo = True
            break

    if not negativo:
        print('S')
    
