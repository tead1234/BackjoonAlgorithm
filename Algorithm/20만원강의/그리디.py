import sys

input = sys.stdin.readline
n = int(input())
B = sorted(map(int, input().split()))
A = sorted(map(int, input().split()))
ans = 0
key = 0
if B[0] > A[n - 1]:
    print(0)
else:
    for a in A:
        if a > B[key]:
            ans += 1
            key += 1
            continue
    print(ans)

