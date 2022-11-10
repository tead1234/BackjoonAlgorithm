N, C = map(int,input().split())
L = []

for _ in range(N):
    L.append(int(input()))
L.sort()
st = 1
end = L[-1] - L[0]

ans = 0
while st <= end:
    mid = (st+end) // 2
    val = L[0]
    cnt = 1
    for i in range(1,N):
        if L[i] >= val + mid:
            val = L[i]
            cnt += 1
    if cnt >= C:
        st = mid + 1
        ans = mid
    elif cnt < C:
        end = mid -1


print(ans)


## parametic서치라는데 이게 뭐냐 씨발