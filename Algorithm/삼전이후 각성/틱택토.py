def Count(board):
    o_cnt = 0
    x_cnt = 0
    for i in board:
        for j in i:
            if j == 'O':
                o_cnt += 1
            elif j == 'X':
                x_cnt += 1

    if o_cnt == x_cnt + 1:
        return 2
    elif o_cnt == x_cnt:
        return 1
    else:
        return 0


def check(board):
    ## o나 x가 등장하면 상하좌우 대각선으로 탐색해서 3개가 채워지는지 확인
    ## 완성횟수도
    cnt_o = 0
    cnt_x = 0
    # o로 완성될 경우 전부
    if board[0][0] == 'O':
        # 오른쪽, 아래 , 대각선
        if board[1][0] == 'O' and board[2][0] == 'O':
            cnt_o += 1
        elif board[0][1] == 'O' and board[0][2] == 'O':
            cnt_o += 1
        elif board[1][1] == 'O' and board[2][2] == 'O':
            cnt_o += 1
    if board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        cnt_o += 1
    if board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        cnt_o += 1
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        cnt_o += 1
    if board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        cnt_o += 1
    if board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        cnt_o += 1
    if board[0][0] == 'X':
        # 오른쪽, 아래 , 대각선
        if board[1][0] == 'X' and board[2][0] == 'X':
            cnt_x += 1
        elif board[0][1] == 'X' and board[0][2] == 'X':
            cnt_x += 1
        elif board[1][1] == 'X' and board[2][2] == 'X':
            cnt_x += 1
    if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        cnt_x += 1
    if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        cnt_x += 1
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        cnt_x += 1
    if board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        cnt_x += 1
    if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        cnt_x += 1
    return cnt_o, cnt_x


def solution(board):
    ## 정상적으로 규칙을 지켰을때 나올수 있는 게임판은
    ## o의 갯수가 x 보다 1크거나같고
    # 틱택토 완성이 오직 하나의 도형에서만 일어나야됨
    B = []
    for b in board:
        B.append(list(b))

    c, d = check(B)
    if Count(B) == 2:
        if (c == 0 and d == 0) or (c == 1 and d == 0) or (c == 2 and d == 0):
            return 1
        else:
            return 0
    elif Count(B) == 1:
        if (c == 0 and d == 0) or (c == 0 and d == 1):
            return 1
        else:
            return 0
    else:
        return 0