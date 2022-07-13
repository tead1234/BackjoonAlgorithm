N = int(input())
d = [-1] * (N+5)
d[0] = 1
d[1] = 2
d[2] = 3
d[3] = 4
d[4] = 5
li = []
for i in range(5, N):
    li = []
    for j in range(0, i):
        for k in range(0,i):
            a = d[j] * d[k]
            if a not in d and a > 0:
                li.append(a)
    b = min(li)
    d[i] = b

print(d[N-1])
