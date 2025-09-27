n = int(input())
    
def fibo(n:int):
    fibo = [0, 1]
    if n == 0 or n ==1:
        fibo = [n]
    else:
        for i in range(n-1):
            fibo.append(fibo[i] + fibo[i+1])
    print(f"Fib({n}) = {fibo[-1]}")

for i in range(n):
    f = int(input())
    fibo(f)