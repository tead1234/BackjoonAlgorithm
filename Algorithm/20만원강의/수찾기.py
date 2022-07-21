N = int(input())
합 = 0
maximal_sum = 0
mx_index = -1
li = sorted(list(map(int, input().split())))
## 최빈값
for i in range(N):
    for j in range(i, N):
        if li[i] == li[j]:
            합 += 1
            if 합 == maximal_sum:
                if i > mx_index:
                    maximal_sum = sum
                    mx_index = i
            elif 합 > maximal_sum:
                maximal_sum = sum
                mx_index = i
mx = sum(li)

print(mx // N)
print(li[N // 2])
print(li[mx_index])
print(li[N - 1] - li[0])
