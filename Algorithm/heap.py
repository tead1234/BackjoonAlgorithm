import heapq

def sorting(jobs,time):
    test = []
    jobs2 = jobs.copy()
    key = len(jobs2)
    for i in range(len(jobs2)):
        a, b = jobs2[i]
        if a <= time:
            continue
        else:
           key = i
           break
    test = jobs2[0:key]
    del jobs2[0:key]
    return test

def solution(jobs):
    time = 0
    작업시간 = 0
    test = []
    N = len(jobs)
    heapq.heapify(jobs)
    t1, t2 = heapq.heappop(jobs)
    time = time + t1 + t2
    작업시간 += t2
    while jobs:
        ## 첫작업을 마쳤을때 대기하고 있는 job이 있다면
        jobs = sorted(jobs, key=lambda x: x[0])
        test = sorting(jobs,time)

        if not len(test) == 0:
            test = sorted(test, key=lambda x: x[1])
            t1, t2 = heapq.heappop(test)
            jobs.remove([t1,t2])
            작업시간 = time - t1 + t2 + 작업시간
            time += t2
            test = []
        else:
            heapq.heapify(jobs)
            t1, t2 = heapq.heappop(jobs)
            작업시간 = t2 + 작업시간
            time = t1 - time + t2 + time


    return 작업시간//N


print(solution( [[0,3],[4,4],[5,3],[4,1]]))
