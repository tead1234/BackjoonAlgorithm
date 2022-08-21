n,m = map(int,input().split())
MAP = list(map(int,input().split()))
Dice = list(map(int,input().split()))
## 0에서 출발
st = 0
flag = False
for i in range(len(Dice)):
	if Dice[i] % 2 == 0:
		if Dice[i] + st >= n-1:
			st = n
			print(st)
			flag = True
			break
		else:
			st += Dice[i]
			if MAP[st] != 0:
				st += MAP[st]
	else:
		if st - Dice[i] >= 0:
			st -= Dice[i]
			if MAP[st] != 0:
				st += MAP[st]
		else:
			st = 0
if flag == False:
	print(st+1)