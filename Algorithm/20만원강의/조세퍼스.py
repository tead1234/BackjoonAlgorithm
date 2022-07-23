from collections import deque
m,n = map(int,input().split())
ans = []
리스트 = deque()
for i in range(m):
	리스트.append(i+1)

while 리스트:
    for i in range(0,n-1):
        리스트.append(리스트.popleft())
    ans.append(리스트.popleft())
print(str(ans).strip("[]").replace(",", ""))