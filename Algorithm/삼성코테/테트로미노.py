N, M = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(N)]
## 초기 모형 설정
# 각 도형모양으로 색칠해주는 함수
def space_bar((x,y)):
    ## x,y는 무조건 되는 애들만 넣기
    MAX = 0
    space = []
    MAXLIST = []
    ## 정배열
    if M > y + 3 >= 0:
        for j in range(4):
            space.append((x,y+j))

        for i in range(4):
            MAX += G[x][y+i]
        MAXLIST.append(MAX)
    # 시계방향 90 회전하기
    for _ in range(3):
