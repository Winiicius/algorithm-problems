n = int(input())

for i in range(n):
    p = str(input())
    pp = p[:int(len(p)/2)]
    sp = p[int(len(p)/2):]

    print(pp[::-1], sp[::-1], sep="")