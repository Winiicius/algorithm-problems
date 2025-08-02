n = int(input())

for i in range(n):
    qtd_prod = int(input())
    prod_dict = {}
    for j in range(qtd_prod):
        prod_val = str(input())
        prod, val = prod_val.split()
        prod_dict[prod] = float(val)
    dona_maria = int(input())
    total:float = 0

    for h in range(dona_maria):
        prod_qtd = str(input())
        prod_dona, qtd = prod_qtd.split()
        total += prod_dict[prod_dona] * int(qtd)
    print(f"R$ {total:.2f}")


    
