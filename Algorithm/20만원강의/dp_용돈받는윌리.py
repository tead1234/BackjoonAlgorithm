n = int(input())
work = [list(map(int,input().split())) for _ in range(n)]
# 전주에 했던 걸 제외하고 선택하면 되지 않을까??
##  key 를 정해서 해당 키가 골라지면 pass시키면될듯?
## d는 주차별 최대 이익
d = [[0,0,0] for _ in range(n)]
print(d)
for k in range(n):
	for l in range(3):
		d[k][l] = 0
d[0][0] = work[0][0]
d[0][1] = work[0][1]
d[0][2] = work[0][2]
print(d)
for i in range(1,n):
	d[i][0] = max(d[i-1][1], d[i-1][2]) + work[i][0]
	d[i][1] = max(d[i-1][0], d[i-1][2]) + work[i][1]
	d[i][2] = max(d[i-1][0], d[i-1][1]) + work[i][2]
print(max(d[n-1]))