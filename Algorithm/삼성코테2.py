## 홀수 숫자가 주어지고 그 크기의 2차원 배열이 주어짐
## 각 구역마다 숫자가 있어서 하나의 영역을 차지함 가운데 N-1/2 라인에 있는 애들만 빼고 나머지 애들은 시계방향으로 회전
## 가운데 라인애들은 시계 반대 방향으로 회전함
## 열융합 발열 액은 각 구간 (A점수+ B점수) * 겹치지는 벽구간 + (A의 구역크기+ B의 구역크기)
## 저짓을 4번했을때 점수의 합을 가져와야됨

N = int(input())
## 그래프 입력받기
graph = [list(map(int,input().split())) for _ in range(N)]
graph2 = [[0]*N for _ in range(N)]
## 2차원배열이 시계방향으로 움직이는건 0,0 => 0,1 90도 회전은 변경전 열이 변경후 행으로 변경전 N-1 - 변경전 행 == 변경후 열

def turn_90(배열):
    for i in range(N):
        for j in range(N):
            ## 시계 반대방향 회전
            ## 시계방향 회전이면 0,0 => 2,0 0,1>>2,1  1,0 => 0,1 2,0 = 0,0 2,1 >> 1,0 1,2 = 2, 1

            graph2[j][N-1-i] = graph[i][j]
    return graph2
def copy(바꾸는배열, 바뀌는배열):
    for i in range(len(바꾸는배열)):
        for j in range(len(바꾸는배열)):
            바뀌는배열[i][j] = 바꾸는배열[i][j]
    return 바뀌는배열

## N이

print(copy(turn_90(graph),graph))

