from collections import deque
## X가 있는 g의 점을 찾아서 그 부분을 전부 o로 칠하고
## 1로 칠한 곳에서 부터 bfs floodfill로 거리 계산
## X를 다시 만나면 그떄 값을 출력
q = deque()
n,m = map(int,input().split())
g = [list(input()) for _ in range(n)]
vis_g = [[0] * m for _ in range(n)]
flag = False
dist = [[0] * m for _ in range(n)]
L= []
def find(x):
	global dist
	ans = 0
	Q = deque(x)

	while Q:
		a,b = Q.popleft()

		dx = [-1, 0, 1, 0]
		dy = [0, -1, 0, 1]
		for k in range(4):
			if n > dx[k] + a >= 0 and m > dy[k] + b >= 0:
				if g[dx[k] + a][dy[k] + b] == '.':
					if dist[dx[k] + a][dy[k] + b] ==0:
						dist[dx[k] + a][dy[k] + b] = dist[a][b] + 1
						Q.append((dx[k] + a,dy[k] + b))
				elif g[dx[k] + a][dy[k] + b] == 'X':
					ans = dist[a][b]
					return ans





def paint(x):

	i,j = x
	vis_g[i][j] = 1
	g[i][j] = 'o'
	q.append((i,j))
	dx = [-1,0,1,0]
	dy = [0,-1,0,1]
	while q:
		I,J = q.popleft()
		for k in range(4):
			if n>dx[k] + I>=0 and m> dy[k]+J>= 0:
				if g[dx[k] + I][dy[k] + J] == 'X' and vis_g[dx[k] + I][dy[k] + J] != 1:
					g[dx[k] + I][dy[k] + J] = 'o'
					vis_g[dx[k] + I][dy[k] + J] = 1
					q.append((dx[k] + I,dy[k] + J))
for i in range(n):
	for j in range(m):
		if g[i][j] == 'X' and flag == False:
			paint((i,j))
			flag = True
## bfs로 거리 찾기
for I in range(n):
	for J in range(m):
		if g[I][J] == 'o':
			L.append((I,J))

print(find(L))



