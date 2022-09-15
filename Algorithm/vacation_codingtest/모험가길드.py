N = int(input())
List = sorted(map(int,input().split()), reverse= True)
# print(List)
ans = 0
while List:
    a = List[0]
    del List[:a]
    ans += 1
print(ans)