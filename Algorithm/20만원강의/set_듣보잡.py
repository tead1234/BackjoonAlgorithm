n,m = map(int,input().split())
듣 = [input() for _ in range(n)]
#print(듣)
보 = [input() for _ in range(m)]
#print(보)
a = len(듣) + len(보)
잡 = len(set(듣 + 보))
print(a - 잡)
## 이유 >> set을 쓰면 겹치는 애들이 줄어듬 >> 즉 전체 배열에서 겹치는 애들 (답) 만큼 빠짐
## 따라서 >> 이전 개수와 set이후 갯수를 빼면 답답
## set. add , set.remove 없는 거 지우려면 에러 뜸 >> set.discard 없는걸 지우라고 하면 그냥 패스