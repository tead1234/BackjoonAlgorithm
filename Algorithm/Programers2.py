from collections import deque


def solution(progresses, speeds):
    answer = []
    cnt = 0
    pro = -1
    a = deque()
    for i in range(len(progresses)):
        for b in range(1, 101):
            if 100 <= progresses[i] + (speeds[i] * b):
                a.appendleft(b)
                break

    for _ in range(len(a)):
        if a:
            if pro == -1:

                pro = a.pop()
                aft = pro
            pro = a.pop()
            if pro <= aft:
                cnt += 1
            else:## eof 면 바로 탈출 어떻게 만들ㅈ디???
                cnt+=1
                answer.append(cnt)
                aft = pro
                cnt = 0

        else:
            cnt+=1
            answer.append(cnt)
            break
    return answer


print(solution(	[93, 30, 55],	[1, 30, 5]))
