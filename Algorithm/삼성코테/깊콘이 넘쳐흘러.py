import heapq
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C=[(a,b) for a,b in zip(A,B)]
heapq.heapify(C)

ex = 30
## 연장핫는 경우
## 써야되느 시간이 왔는데
ans = 0
while C:
    x, y = heapq.heappop(C)

    if x  < y:
        x += ex
        print(x,y)
        heapq.heappush(C,(x,y))
        ans += 1
    else:
        continue

print(ans)
