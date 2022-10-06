from collections import deque
N, C = map(int, input().split())
M = int(input())
List = [list(map(int, input().split())) for _ in range(M)]
loaded = C
loadedList = deque()
List = sorted(List, key=lambda x: (-x[0], -x[1], x[2]))
print(List)
q = deque()
for L in List:
    if loaded == 0:
        break
    a,b,c = List.pop()
    if loaded >= c:
        loaded -= c
        loadedList.append((b,c))
    else:
        k = loaded
        loaded = 0
        loadedList.append((b,k))

# 배달갯수
ans = 0
# 첨음 q에 넣을 배달 목적지

while List:
    e,w = loadedList.popleft()
    if e == N and len(loadedList) == 0:
        break
    else:
        # 방문 리스트에서 e값을 가진 애가 있는지파악
        loaded += w
        ans += w

        if len(List) != 0:
            if List[-1][0] == e:
                for L in List:
                    if L[0] == e:
                        if loaded == 0:
                            break
                        a, b, c = List.pop()
                        if loaded >= c:
                            loaded -= c
                            loadedList.append((b, c))
                        else:
                            k = loaded
                            loaded = 0
                            loadedList.append((b, k))
                    else:
                        continue
            # 배달후에 다음 화물이 다음 장소에 있을경우
            else:
                if loaded == 0:
                    continue



while loadedList:
    r,t = loadedList.popleft()
    ans += t

print(ans)