from collections import deque
N = int(input())
A = input().split()
A = deque(sorted(A, reverse=True))
answer = 0
while A:
    i = A.popleft()
    if int(i) <= len(A) + 1:
        for _ in range(int(i)-1):
            A.popleft()
    else:
        break
    answer += 1

print(answer)