## 홀수 숫자가 주어지고 그 크기의 2차원 배열이 주어짐
## 각 구역마다 숫자가 있어서 하나의 영역을 차지함 가운데 N-1/2 라인에 있는 애들만 빼고 나머지 애들은 시계방향으로 회전
## 가운데 라인애들은 시계 반대 방향으로 회전함
## 열융합 발열 액은 각 구간 (A점수+ B점수) * 겹치지는 벽구간 + (A의 구역크기+ B의 구역크기)
## 저짓을 4번했을때 점수의 합을 가져와야됨

N = int(input())
## 그래프 입력받기
K = N//2
graph = [list(map(int,input().split())) for _ in range(N)]
## 2차원배열이 시계방향으로 움직이는건 0,0 => 0,1 90도 회전은 변경전 열이 변경후 행으로 변경전 N-1 - 변경전 행 == 변경후 열

def turn_90(graph):
    graph2 = graph.copy()
    for i in range(len(graph)):
        for j in range(len(graph)):
            graph2[j][len(graph)-1-i] = graph[i][j]
    return graph2

def slice_list(startX,startY, endX,endY, graph):
    # 행이랑 동시에 슬라이싱이 안되네
    graph2 = []
    graph = graph[startX:startY+1]
    for i in range(0, endY- endX+1):
        graph2.append(graph[i][endX:endY+1])
    return  graph2


## N이
print(slice_list(0,0,1,1,graph))
# print(turn_90())

