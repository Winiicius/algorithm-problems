def main(n):
    count = 0
    for i in range(n):
        count += str(i).count("1")
    return count


def imobi(prices):
    lucro_atual = -prices[0]
    lucro_maximo = 0

    for i in prices[1:]:
        lucro_atual = max(lucro_atual, lucro_atual-i)
        lucro_maximo = max(lucro_maximo, lucro_atual)

    return lucro_maximo

def majoritaryElement(nums:list):
    candidato = 0
    count = 0
    for n in nums:
        if count == 0:
            candidato = n
        count += (1 if n == candidato else -1)

    return candidato


print(majoritaryElement([1,2,3,4,5,4,3,2,1,2,3,2,3,2,2,1,2,5]))

def panda(piles, h):
    maior = max(piles)
    if(h == len(piles)):
        return maior
    
    count = 0
    for pile in piles:
        count += pile // h
        if pile % h != 0:
            count += 1
    
    aux = 0
    melhor = h
    k = 1
    while True:
        r = 0
        for pile in piles:
            r += pile - k
            if r <= 0:
                

            

    return count
        
print(panda([30,11,23,4,20], 6))

def displayTable(orders):
    mesas = {}  # mesa -> item -> quantidade
    items = set()

    # Preencher os dados
    for nome, mesa, item in orders:
        if mesa not in mesas:
            mesas[mesa] = {}
        if item not in mesas[mesa]:
            mesas[mesa][item] = 0
        mesas[mesa][item] += 1

        items.add(item)

    items = sorted(items)  # cabeçalho em ordem alfabética
    header = ["Table"] + items
    resultado = [header]

    # adicionar linhas por mesa, ordenando mesas numericamente
    for mesa in sorted(mesas.keys(), key=int):
        linha = [mesa]
        for item in items:
            linha.append(str(mesas[mesa].get(item, 0)))
        resultado.append(linha)

    return resultado