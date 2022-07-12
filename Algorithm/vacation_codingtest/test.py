li = list(map(int,input().split()))
li2 = list(map(int,input().split()))
sum_mx = 0
answer = 0
def sum(i,j, li2):
	global answer
	sum = 0
	for k in range(i,j+1):
		sum += li2[k]
		if sum > li[1]:
			return
	if li[1] == sum:
		answer += 1

for i in range(len(li2)):
	for j in range(i, len(li2)):
		sum(i,j,li2)

print(answer)
