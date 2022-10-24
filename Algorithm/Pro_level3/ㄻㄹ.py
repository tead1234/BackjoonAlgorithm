def solution(board):
    answer = -1
    ansL = []
    vis= [[False] * len(board) for _ in range(len(board))]
    def dfs(x,y,depth,visited):
        vis[x][y] = True
        dir = [(-1,0),(0,-1),(1,0),(0,1)]
        for k in range(4):
            dx,dy = dir[k]
            if len(board) > dx+ x >= 0 and len(board) > dy+ y >= 0:
                if board[dx+ x][dy+ y] == board[x][y] and visited[dx+ x][dy+ y] == False:
                    dfs(dx+ x,dy+ y,depth+1,visited)
                    visited[dx+ x][dy+ y] = False
        ansL.append(depth)
    for i in range(len(board)):
        for j in range(len(board)):
            dfs(i,j,1,vis)
            vis = [[False] * len(board) for _ in range(len(board))]
    answer = max(ansL)
    if answer == 1:
        return -1
    else:
        return answer

## 재밋게도 배열을 넣으면 그 상태가 저장돼서 나오네 ??

print(solution([[3, 2, 3, 2], [2, 1, 1, 2], [1, 1, 2, 1], [4, 1, 1, 1]]))