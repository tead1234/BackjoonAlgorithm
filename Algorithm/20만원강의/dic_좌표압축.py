import sys
input = sys.stdin.readline
n = int(input())
p  = list(map(int,input().split()))
p1  = sorted(list(set(p)))
dic = {}
## set쓰면 nlogn 1000000 * 1000 => 1억 >> 파이썬은 1초에 4천만 >> 2.5초 걸림
for i,a in enumerate(p1):
	dic[a] = i
for a in p:
	print(dic[a], end = " ")