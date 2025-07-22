a, b = list(map(int, input().split()))

for i in range(1, b+1):
    print(i, end="")
    if(i % a == 0):
        print()
        continue
    print(" ", end="")