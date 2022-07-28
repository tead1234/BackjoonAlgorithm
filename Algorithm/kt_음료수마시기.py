from collections import deque
def bfs(list, I , p):
    q = deque()
    visited = []
    ans = []
    s = 0
    ## 각 이름표를 붙여야함
    for i in range(len(list)):
        visited.append(list[i][0])
    q.append(I)
    while q:
        n, l, c, r = q.popleft()
        ## 여분이 있고 p보다 열량이 낮다면
        if l < p and visited[r] != 0:
            p -= l
            visited[r] -= 1
            s += c
            for li in list:
                q.append(li)
        elif l>=p :
            s += c
            return s





## 사용할수 있는 음료수들만 담는 배열
## 각 리터당 최대의 열량을 내는 애들을 우선 배치
def solution(list, p):
    ## dp문제 list는 각각 갯수, 리터, 열량으로 구성
    ## p만큼으로 만들수 있는 최대열량 배열을 만들고 p+1의 값은 남은 음료중에 가장 큰 값을 가진 애를 더하면 되나??
    ## 남은 음료수 배열,
    for a,i in enumerate(list):
        i.append(a)
        print(bfs(list, i, p))

print(solution([[1,3,5],[5,1,2], [1,1,1], [3,2,2]], 3))