N = int(input())
d = [0] * (N+1)
## 1
d[1] =0
## 2
d[2] = 1
li = []
for i in range(3, N+1):
    if i % 2 == 0:
        li.append((d[i//2] + 1))
    elif i % 5 == 0:
        li.append((d[i//5] + 1))
    elif i % 3 == 0:
        li.append((d[i//3]+1))
    li.append((d[i-1]+ 1))
    d[i] = min(li)
    li = []
print(d)