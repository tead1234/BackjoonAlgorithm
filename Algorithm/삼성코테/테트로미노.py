N, M = map(int,input().split())
G = [list(map(int,input().split())) for _ in range(N)]
## 초기 모형 설정
# 각 도형모양으로 색칠해주는 함수
def space_bar(x, y, k):
    ## x,y는 무조건 되는 애들만 넣기
    MAX = 0
    space = []
    MAXLIST = []
    flg = False
    ## 스페이스바
    if k == 0:
        space = [(x,y),(x,y+1),(x,y+2),(x,y+3)]
        for k in space:
            o,p =k
            if N > o >= 0 and M > p >= 0:
                continue
            else:
                flg= True

        if flg != True:
            for i in space:
                spc_x, spc_y = i
                MAX += G[spc_x][spc_y]
            MAXLIST.append(MAX)
            MAX = 0
            test = []
        else:
            flg = False
            test = []


    elif k == 1:
        for i in range(2):
            for j in range(2):
                    space.append((x + i,y+j))
        for k in space:
            o, p = k
            if N > o >= 0 and M > p >= 0:
                continue
            else:
                flg = True

        if flg != True:
            for i in space:
                spc_x, spc_y = i
                MAX += G[spc_x][spc_y]
            MAXLIST.append(MAX)
            MAX = 0
            test = []
        else:
            flg = False
            test = []
    # 니은 도형
    elif k == 2:
        List = [(x,y),(x+1,y),(x+2,y),(x+2,y+1)]
        for L in List:
            L_x, L_y = L
            if N > L_x >=0 and M > L_y >= 0:
                continue
            else:
                flg =True

        space = List.copy()
        List = []
        if flg != True:
            for i in space:
                spc_x, spc_y = i
                MAX += G[spc_x][spc_y]
            MAXLIST.append(MAX)
            MAX = 0

            test = []
        else:
            flg = False
            test = []
    # 애벌레
    elif k == 3:
        List = [(x,y),(x+1,y),(x+1,y+1),(x+2,y+1)]
        for L in List:
            L_x, L_y = L
            if N > L_x >= 0 and M > L_y >= 0:
                continue
            else:
                flg = True

        space = List.copy()
        List = []
        if flg != True:
            for i in space:
                spc_x, spc_y = i
                MAX += G[spc_x][spc_y]
            MAXLIST.append(MAX)
            MAX = 0

            test = []
        else:
            flg = False
            test = []
    elif k ==4:
        List = [(x, y), (x, y+1), (x + 1, y + 1), (x , y + 2)]
        for L in List:
            L_x, L_y = L
            if N > L_x >= 0 and M > L_y >= 0:
                continue
            else:
                flg = True
                break
        space = List.copy()
        List = []
        if flg != True:
            for i in space:
                spc_x, spc_y = i
                MAX += G[spc_x][spc_y]
            MAXLIST.append(MAX)
            MAX = 0

            test = []
        else:
            flg = False
            test = []
    #
    # print(space)
    ## 정배열
        # 시계방향 90 회전하기
    for _ in range(4):
        # space 제일 앞이 꼭지점이고
        # pop을 잘못하면 원배열 복구가 불가능
        space_copy = space.copy()
        test = []
        for i,a in enumerate(space_copy):
            if i == 0:
                # peek
                peek_x, peek_y = a
                continue
            X,Y = a
            #꼭지점만큼 이동
            X -= peek_x
            Y -= peek_y
            test.append((Y + peek_x, peek_y-X))
        for i in range(1,4):
            space[i] = test[i-1]
        for k in space:
            o,p =k
            if N > o >= 0 and M > p >= 0:
                continue
            else:
                flg= True
                break
        if flg != True:
            for i in space:
                spc_x, spc_y = i
                MAX += G[spc_x][spc_y]
            MAXLIST.append(MAX)
            MAX = 0

            test = []
        else:
            flg = False
            test = []
            continue
    ## 좌우 대칭이동

        # space 제일 앞이 꼭지점이고
        # pop을 잘못하면 원배열 복구가 불가능
    space_copy = space.copy()
    test = []
    for i,a in enumerate(space_copy):
        if i == 0:
            # peek
            peek_x, peek_y = a
            continue
        X,Y = a
        #꼭지점만큼 이동
        X -= peek_x
        Y -= peek_y

        test.append((X + peek_x,peek_y -Y))

    for i in range(1,4):
        space[i] = test[i-1]
    for k in space:
        o, p = k
        if N > o >= 0 and M > p >= 0:
            continue
        else:
            flg = True
            break
    if flg != True:
        for i in space:
            spc_x, spc_y = i
            MAX += G[spc_x][spc_y]
        MAXLIST.append(MAX)
        MAX = 0
        flg = False
        test = []
    else:
        test = []

    # 시계방향 90 회전하기
    for _ in range(4):
        # space 제일 앞이 꼭지점이고
        # pop을 잘못하면 원배열 복구가 불가능
        space_copy = space.copy()
        test = []
        for i, a in enumerate(space_copy):
            if i == 0:
                # peek
                peek_x, peek_y = a
                continue
            X, Y = a
            # 꼭지점만큼 이동
            X -= peek_x
            Y -= peek_y
            test.append((Y + peek_x, peek_y - X))
        for i in range(1, 4):
            space[i] = test[i - 1]
        for k in space:
            o, p = k
            if N > o >= 0 and M > p >= 0:
                continue
            else:
                flg = True
                break
        if flg != True:
            for i in space:
                spc_x, spc_y = i
                MAX += G[spc_x][spc_y]
            MAXLIST.append(MAX)
            MAX = 0
            flg = False
            test = []
        else:
            test = []
            continue
    # 상하 이동

        # space 제일 앞이 꼭지점이고
        # pop을 잘못하면 원배열 복구가 불가능
    space_copy = space.copy()
    test = []
    for i,a in enumerate(space_copy):
        if i == 0:
            # peek
            peek_x, peek_y = a
            continue
        X,Y = a
        #꼭지점만큼 이동
        X -= peek_x
        Y -= peek_y

        test.append(( peek_x- X, peek_y - Y))

    for i in range(1, 4):
        space[i] = test[i - 1]
    for k in space:
        o, p = k
        if N > o >= 0 and M > p >= 0:
            continue
        else:
            flg = True
            break
    if flg != True:
        for i in space:
            spc_x, spc_y = i
            MAX += G[spc_x][spc_y]
        MAXLIST.append(MAX)
        MAX = 0
        flg = False
        test = []
    else:
        test = []
    for _ in range(4):
        # space 제일 앞이 꼭지점이고
        # pop을 잘못하면 원배열 복구가 불가능
        space_copy = space.copy()
        test = []
        for i, a in enumerate(space_copy):
            if i == 0:
                # peek
                peek_x, peek_y = a
                continue
            X, Y = a
            # 꼭지점만큼 이동
            X -= peek_x
            Y -= peek_y
            test.append((Y + peek_x, peek_y - X))
        for i in range(1, 4):
            space[i] = test[i - 1]
        for k in space:
            o, p = k
            if N > o >= 0 and M > p >= 0:
                continue
            else:
                flg = True
                break
        if flg != True:
            for i in space:
                spc_x, spc_y = i
                MAX += G[spc_x][spc_y]
            MAXLIST.append(MAX)
            MAX = 0
            flg = False
            test = []
        else:
            test = []
    if len(MAXLIST) != 0:
        ans = 0
        ans =max(MAXLIST)

    else:
        ans = 0

    return ans
ANSWER = 0
O = 0
for i in range(N):
    for j in range(M):
        for k in range(5):
            O = space_bar(i, j,  k)
            if ANSWER < O:
                ANSWER = O
print(ANSWER)
# space_bar(0,  4,  0)