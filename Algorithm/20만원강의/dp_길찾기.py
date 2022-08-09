N= int(input())
g= [list(input()) for _ in range(N)]
d = [[0] * N for _ in range(N)]
d[0][0] = 0
## 다 막힌 경우에도 갈수 있다고 판단되네
for c in range(N):
	if g[0][c] != "*":
		d[0][c] = 1
	else:
		break
for c in range(N):
	if g[c][0] != "*":
		d[c][0] = 1
	else:
		break
for k in range(1,N):
	for j in range(1,N):
		if N>k-1>=0 and N>j-1>=0 and g[k][j] != "*":
			d[k][j] = (d[k-1][j] + d[k][j-1]) % 1000000007
print(d[N-1][N-1])