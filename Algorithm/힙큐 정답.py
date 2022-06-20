import heapq

def solution(jobs):
    answer = 0
    jobs.sort()
    start = jobs[0][0]
    jobHeapq = []
    check = [False for i in range(len(jobs))]

    # 0초 기준으로 맞춤
    for i,value in enumerate(jobs):
        jobs[i][0] -= start


    answer += jobs[0][1]
    end = jobs[0][1]
    check[0] = True
    cnt = 1
    lastIndex = 0

    while cnt < len(jobs):
        for i,value in enumerate(jobs):
            #작업 중일때 요청들어온 디스크 작업
            if value[0] <= end and check[i] == False:
                heapq.heappush(jobHeapq,[value[1],i])
                check[i] = True
            elif value[0] > end:
                lastIndex = i
                break

        if len(jobHeapq)==0: #디스크에 작업이 없을 경우
                answer += (jobs[lastIndex][1])
                end = jobs[lastIndex][1] +jobs[lastIndex][0]
                check[lastIndex]= True
                lastIndex+=1
                cnt+=1
        else:
            #minheaq[0] = 소요시간 , minheaq[1] = 디스크 인덱스
            minheaq = heapq.heappop(jobHeapq)
            answer += (minheaq[0]+end-jobs[minheaq[1]][0])
            end += minheaq[0]
            cnt+=1

    # answer = int(answer/len(jobs))
    return answer

print(solution([[0,10],[4,10],[5,11],[15,2]]))