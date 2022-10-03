def solution(commands):
    ## update가 나오면 append
    ## merge가 나오면 주소값을
    ## unMERge가 나오면
    data = [[[0] for _ in range(50)] for _ in range(50)]
    answer = []
    for com in commands:
        com = com.split()
        if com[0] == 'UPDATE':
            ## 전부 문자열이니깐 저걸론 구분 불가
            if len(com) == 3:
                for i in range(50):
                    for j in range(50):
                        if data[i][j][0] == com[1]:
                            data[i][j][0] = com[2]
            else:
                if len(data[int(com[1])-1][int(com[2])-1]) >= 2:
                    data[int(com[1]) - 1][int(com[2]) - 1][0] = com[3]
                    for a in range(1,len(data[int(com[1])-1][int(com[2])-1])):
                        c,d = data[int(com[1]) - 1][int(com[2]) - 1][a]
                        data[c][d][0] = com[3]
                else:
                    data[int(com[1]) - 1][int(com[2]) - 1][0] = com[3]
        elif com[0] == 'MERGE':
            ## 값을 가지는 애로 병합하는거 추가 하고
            ## 주소값도 공유해 줘야하고

            ## 병합된걸 파악하려면 길이가 2이상이고 첫번째 수가 0이여야함
            x = int(com[1]) -1
            y = int(com[2]) -1
            z=  int(com[3]) -1
            w = int(com[4]) - 1
            ## 합병하는 곳에 주소넣기
            if data[x][y][0] != 0:
                data[z][w][0] = data[x][y][0]
                data[z][w].append([x,y])
                data[x][y].append([z,w])
                if len(data[z][w]) > len(data[x][y]):
                    for da in data[x][y]:
                        if da not in data[z][w]:
                            data[z][w].append(da)
                    data[x][y] = data[z][w]
                else:
                    for da in data[z][w]:
                        if da not in data[x][y]:
                            data[x][y].append(da)
                    data[z][w] = data[x][y]
            else:
                data[z][w].append([x, y])
                data[x][y].append([z, w])
                if data[z][w][0] == 0:
                    data[z][w][0] = data[x][y][0]
                    if len(data[z][w]) > len(data[x][y]):
                        for da in data[x][y]:
                            if da not in data[z][w]:
                                data[z][w].append(da)
                        data[x][y] = data[z][w]
                    else:
                        for da in data[z][w]:
                            if da not in data[x][y]:
                                data[x][y].append(da)
                        data[z][w] = data[x][y]
                else:
                    data[x][y][0] = data[z][w][0]
                    if len(data[z][w]) > len(data[x][y]):
                        for da in data[x][y]:
                            if da not in data[z][w]:
                                data[z][w].append(da)
                        data[x][y] = data[z][w]
                    else:
                        for da in data[z][w]:
                            if da not in data[x][y]:
                                data[x][y].append(da)
                        data[z][w] = data[x][y]

        elif com[0] == 'UNMERGE':
            u= int(com[1]) -1
            o =int(com[2]) - 1
            for a in range(len(data[u][o])):
                if a != 0:
                    X,Y = data[u][o][a]
                    if X == u and Y == o:
                        continue
                    data[X][Y] = [0]
                else:
                    save = data[u][o][0]
            data[u][o] = [0]
            data[u][o][0] = save




        elif com[0] == 'PRINT':

            if data[int(com[1]) - 1][int(com[2]) - 1][0] == 0:

                answer.append("EMPTY")

            else:

                answer.append(str(data[int(com[1]) - 1][int(com[2]) - 1][0]))

    return answer

print(solution(

["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))