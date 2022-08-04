n = int(input())
List = sorted(list(map(int,input().split())))
def find(x):
	ans = 0
	for a in List:
		ans += abs(a-x)
	return ans
if find(List[n//2]) > find(List[n//2 - 1]):
	print(List[n//2 - 1])
elif find(List[n//2]) == find(List[n//2 - 1]):
	print(List[n//2 - 1])
else:
	print(List[n//2 ])