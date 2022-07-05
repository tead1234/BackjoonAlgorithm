N = int(input())
tem_max = 0
tem_min = 0
K = 0
while N-1 != K:
    a = int(input())
    K += 1
    b = int(input())
    K += 1
    if a > b:
        if a > tem_max:
            tem_max = a
        if b < tem_min:
            tem_min = b
    else:
        if b > tem_max:
            tem_max = b
        if a < tem_min:
            tem_min = a
print(tem_max - tem_min)