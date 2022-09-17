n = int(input())
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
def isFine(answer, a):
    copy = answer.copy()
    copy.remove(a)
    for ans in copy:
        x,y,a = ans
        if a == 0:
            if y == 0:
                continue
            else:
                ## 기둥설치시 조건 확인 그 자리 아래에 기둥이 있든가
                if [x, y - 1, 0] in copy or [x, y, 1] in copy or [x - 1, y, 1] in copy:
                    continue
                else:
                    return False
        if a == 1:
            if [x, y-1, 0] in copy or [x + 1, y-1, 0] in copy:
                continue
            elif [x - 1, y, 1] in copy and [x + 1, y, 1] in copy:
                continue
            else:
                return False
    return True

def solution(n,build_frame):

    answer = []
    for frame in build_frame:
        x,y,a,b = frame
        if b == 1:
            if a == 0:
                if y == 0:
                    answer.append([x, y, a])
                else:
                    ## 기둥설치시 조건 확인 그 자리 아래에 기둥이 있든가
                    if [x,y-1,0] in answer or [x,y,1] in answer or [x-1,y,1] in answer:
                        answer.append([x,y,0])
            ## 보 설치할때 x,y자리에 기둥이 있든가 아니면 x-1,y x+1,y 가 둘다 존재하는가
            if a == 1:
                if [x,y-1,0] in answer or [x+1,y-1,0] in answer:
                    answer.append([x,y,1])
                elif [x-1,y,1] in answer and [x+1,y,1] in answer:
                    answer.append([x,y,1])
        if b == 0:
            if isFine(answer,[x,y,a]):
                answer.remove([x,y,a])
            else:
                continue
    return sorted(answer)

print(solution(5, build_frame))






