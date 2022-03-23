N, K = map(int, input().split())
arr1 = [map(int, input().split())]
arr2 = [map(int, input().split())]

arr1 = sorted(arr1)
arr2 = sorted(arr2)

for i in range(K):
    if arr1[i] <= arr2[K - i-1]:
        if i == K-1:
            break
        arr1[i] = arr2[K - i]


print(arr1)


