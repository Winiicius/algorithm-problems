T = int(input())

for _ in range(T):
    N, C, M = map(int, input().split())
    destinos = list(map(int, input().split()))
    
    destinos.sort(reverse=True)  # maiores primeiro
    energia = 0
    
    for i in range(0, M, C):
        energia += 2 * destinos[i]  # só pega o maior do grupo
    
    print(energia)
