n = int(input())

for i in range(n):
    dic = {}
    frase = str(input());
    for l in frase:
        if l == " ": continue
        letra = l.lower()
        if letra in dic:
            dic[letra] += 1
        else:
            dic[letra] = 1

    result = ""
    valor = max(dic.values())

    for i, k in dic.items():

        if valor == k:
            result += i
        

    print("".join(sorted(result)))


# VERSÃO IA
# from collections import Counter

# n = int(input())

# for _ in range(n):
#     linha = input().lower()

#     # Filtra apenas letras (ignora espaços, números, pontuação etc.)
#     letras = [c for c in linha if c.isalpha()]

#     # Conta a frequência das letras
#     contagem = Counter(letras)

#     # Encontra a maior frequência
#     max_frequencia = max(contagem.values())

#     # Filtra as letras com frequência máxima e ordena
#     mais_frequentes = [letra for letra, freq in contagem.items() if freq == max_frequencia]
#     mais_frequentes.sort()

#     # Imprime como uma única string
#     print("".join(mais_frequentes))
