from itertools import *
## 이문제는 결국 N//2 명을 뽑아서 만들고 그 집단에서 또 2명씩 골라서 능력치를 구한 뒤 팀 능력치를 구해야 하는것

N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]
n = N//2
res = 0
res2 = 0
## 전체 인원을 담아놓는 리스트
total = []
ansList = []
def getSum(A):
    ans = 0
    for a in A:
        for b in A:
            ans += S[a][b]
    return ans

for i in range(N):
    total.append(i)
first = []
second = []
s=list(combinations(total,n))
## second까지 구했고 각 리스트의 합을 구해서 최소 차이가 나도록 구하면 됨
for fir in s:
    first = list(fir)
    second = [x for x in total if x not in first]
    ansList.append(abs(getSum(first) - getSum(second)))
print(min(ansList))
