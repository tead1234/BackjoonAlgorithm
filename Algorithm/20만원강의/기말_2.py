ans = 0
k = int(input())
List = list(map(int,input().split()))
List2 = []

for a in List:
	List2.append(a%3)
vs = [False] * k
for i in range(k):
	if List2[i] == 0 and vs[i] == False:
		vs[i] = True
		ans +=1
		continue
	if List2[i] == 1 and vs[i] == False:
		for j in range(i+1,k):
			if List2[j] == 2 and vs[j]== False:
				ans += 1
				vs[i] = True
				vs[j] = True
				break
	if List2[i] == 2 and vs[i] == False:
		for o in range(i+1,k):
			if List2[o] == 1 and vs[o]== False:
				ans += 1
				vs[i] = True
				vs[o] = True
				break
num = 0
for i in range(len(vs)):
	if vs[i] == False:
		num += 1

ans += num//3
print(ans)