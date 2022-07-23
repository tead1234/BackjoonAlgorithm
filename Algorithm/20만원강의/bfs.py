from collections import deque
x,y = map(int,input().split())
q = deque([x])
ans = 1
visited = deque()
checked = [False] * 10000000
while True:
	a = q.popleft()
	if x == y:
		print(0)
		break
	if x > y:
		print(a-y)
		break
	if checked[a+1] == False :
		checked[a+1] = True
		visited.append(a + 1)
	if checked[a-1] == False :
		checked[a-1] = True
		visited.append(a - 1)
	if checked[a*2] == False :
		checked[a*2] = True
		visited.append(a * 2)
	if checked[y]:
		print(ans)
		break
	if len(visited) != 0 and len(q) == 0:
		ans += 1
		visited2 = visited.copy()
		q = visited2
