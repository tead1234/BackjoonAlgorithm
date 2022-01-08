def solution(n, computers):
    global answer
    answer = n

    def dfs(x, y, n, computers):
        for i in range(4):
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            nx = dx[i]+x
            ny = dy[i]+y
            if x <= -1 or y <= -1 or x >= n  or y >= n:
                return
            if computers[nx][ny] == 1:
                computers[nx][ny] =0
                dfs(ny, ny, n, computers)

        dfs(nx,ny,n,computers)


    for i in range(n):
        if computers[i][i] ==1:
            answer+=1
            dfs(i, i, n, computers)
    return answer




print(solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]))

