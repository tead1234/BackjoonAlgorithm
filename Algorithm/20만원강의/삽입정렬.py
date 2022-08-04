n = int(input())
List = list(map(int,input().split()))
print(str(List).strip("[]").replace(",",""))
for _ in range(n):
    for i in range(n):
        for j in range(i,0, -1):
            if List[i] < List[j]:
                List[j], List[i] = List[i], List[j]
                print(str(List).strip("[]").replace(",",""))