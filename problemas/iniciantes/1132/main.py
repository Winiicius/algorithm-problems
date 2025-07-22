a = int(input())
b = int(input())

maior = max(a, b)
menor = min(a, b)

count = 0
while(menor < maior+1):
    if menor % 13 != 0:
        count += menor
    menor+=1
    
print(count)
