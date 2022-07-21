N = int(input())
g= [int(input()) for _ in range(N)]
## 버블정렬?
for i in range(N):
    for j in range(i,N):
        if g[i] > g[j]:
            g[i], g[j] = g[j], g[i]
for _ in range(N):
    print(g[_])