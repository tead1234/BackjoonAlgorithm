li = list(map(int,input().split()))
li2 = list(map(int,input().split()))
answer = 0
sum = 0
## 여기서 i를 점프시키려면 break 쓰면 가장 가까운 반복문을 종료한다....
for i in range(len(li2)):
	sum = 0
	for j in range(i, len(li2)):
		sum += li2[j]
		if sum == li[1]:
			answer += 1
		elif sum > li[1]:
			break
print(answer)