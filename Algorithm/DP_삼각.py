def solution(triangle):

    d = [[0] * i for i in range(1,501)]
    d[0] = triangle[0][0]
    d[1] = [triangle[1][0] + d[0], triangle[1][1] + d[0]]
    for i in range(2,len(triangle)):
        for j in range(0, i):
            key = d[i - 1][j]
            if d[i][j] < (key + triangle[i][j]):
                d[i][j] = (key + triangle[i][j])
            if d[i][j+1] < (key + triangle[i][j+1]):
                d[i][j+1] = (key + triangle[i][j+1])
    answer = sorted(d[len(triangle)-1], reverse= True)[0]
    return answer

print(solution([[7], [3, 8], [8, 1, 90], [2, 0, 4, 0], [14, 5, 2, 6, 5]]))