n = int(input())
List = list(map(int,input().split()))
print(str(List).strip("[]").replace(",",""))
for _ in range(n):
    for i in range(n-1):
        if List[i] > List[i + 1]:
            List[i+1], List[i] = List[i], List[i+1]
            print(str(List).strip("[]").replace(",",""))
