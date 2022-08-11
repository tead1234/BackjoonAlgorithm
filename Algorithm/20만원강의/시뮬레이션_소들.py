B,E = map(int,input().split())
Blist = [input().split() for _ in range(B)]
Elist = [input().split() for _ in range(E)]
ans= 0
t = 0
bLo = 0
eLo = 0
flag = False
def b_walk(t):
	global bLo
	if len(Blist) <= t:
		return bLo
	b_work = Blist[t]
	dis,d = b_work
	if d == "L":
		bLo -= int(dis)
	else:
		bLo += int(dis)
	return bLo
def e_walk(t):
	global eLo
	if len(Elist) <= t:
		return eLo
	e_walk = Elist[t]
	dis, d = e_walk
	if d == "L":
		eLo -= int(dis)
	else:
		eLo += int(dis)
	return eLo
R = max(E,B)
for t in range(R):
	a = b_walk(t)
	b = e_walk(t)
	if a - b >= 0 and flag == False:
		ans += 1
		flag = True
	elif a- b < 0 and flag == True:
		ans += 1
		flag = False
print(ans)
