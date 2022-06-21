from collections import deque


def solution(jobs):
    총시간 = 0
    before = 0
    작업시간 = 0
    jobs.sort(key=lambda x: x[1])
    for i in range(len(jobs) - 2):
        for j in range(i + 1, len(jobs) - 1):
            if jobs[i][1] == jobs[j][1]:
                if jobs[i][0] > jobs[j][0]:
                    temp = jobs[j]
                    jobs[j] = jobs[i]
                    jobs[i] = temp
    ## 걸리는 시간만 측정하면 될듯?
    # 작업수행시간 - 처음 오더 내려간시간 + 해당 작업 시간

    a,b= jobs[0]
    # 총시간은 첫 작업이 시작 되기 전부터 돌아가는 시간 대기 시간 측정을위함
    총시간 += a + b
    작업시간 += b
    before = 총시간
    for i in range(1,len(jobs)):
        a,b = jobs[i]
        if (총시간 - a) >= 0:
            작업시간 += (총시간 - a) + b

        if (총시간 - a) < 0:
            작업시간 += b
            총시간 += (a - 총시간)
        총시간 += b
    return 작업시간/ len(jobs)
print(solution([[0, 5], [2, 10], [10000, 2]]))