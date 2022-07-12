li = input()
answer = 0
answer2 = 0
for i in range(len(li)-2):
	if li[i:i+3] == 'JOI':
		answer += 1
	if li[i: i+3] == 'IOI':
		answer2 += 1
print(answer)
print(answer2)