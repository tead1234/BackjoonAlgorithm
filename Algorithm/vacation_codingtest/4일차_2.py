li = list(map(int, input().split()))
n = li[0]
k = li[1]
li2 = list(map(int, input().split()))

def dp(li, k):
    d = [0] * (k+1)
    d[0] = 0
    for a in li:
        d[a] = 1
    for i in range(2,k+1):
        minlist = []
        for j in range(1,i):
            if d[i] == 1:
                d[i] = 1
                minlist.append(d[i])
                continue
            minlist.append(d[i-j] + d[j])
        d[i] =sorted(minlist)[0]
    if d[k] ==0:
        return -1
    return d[k]
print(dp(li2, k))

