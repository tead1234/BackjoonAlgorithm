K = int(input())
time = list(map(int,input().split()))
min_k = -1
min_val = 987654
for t in range(len(time)):
    if min_val > time[t]:
        min_val = time[t]
        min_k = t
a = int(time[min_k])
b = int(len(time))
if K - (a * b) < 0:
    K = K%b
while K - (a * b) >= 0:
    if sorted(time, reverse=True)[0] <= 0:
        K = -2
        break
    K -= (a * b)
    min_k = -1
    min_val = 9876552
    cnt = 0
    for i in range(len(time)):
        time[i] -= a
    for a in time:
        if a == 0:
            cnt += 1
    b -= cnt
    for t in range(len(time)):
        if min_val > time[t] > 0:
            min_k = t
            min_val = time[t]
    a = time[min_k]

print(K+1)