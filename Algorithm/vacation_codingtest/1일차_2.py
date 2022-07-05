A = input().split()
N = A[0]
M = A[1]
B = []
min_val = 0
C = [list(map(int, input().split())) for i in range(int(N))]
for res in C:
    min_val = sorted(res)[0]
    B.append(min_val)
for i in range(len(B)):
    if min_val < B[i]:
        min_val = B[i]
print(min_val)