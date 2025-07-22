while(True):
    a, b = list(map(int, input().split()))
    if(a == b): break
    if(a > b): print("Decrescente")
    else: print("Crescente")