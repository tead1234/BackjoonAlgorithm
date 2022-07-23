n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
maxDis = -1
maxXY = [-1,-1]

for i in range(n):
    for k in range(i,n):
        x,y = li[i]
        z,w = li[k]
        dis = abs(x-z) + abs(y-w)
        if dis > maxDis:
            maxDis = dis
            maxXY = [i,k]
ans = [maxXY[0]+1, maxXY[1]+1]
print(str(sorted(ans)).strip("[]").replace(",",""))

