def solution(n, times):

    mid =  1e18
    answer_list = []
    first = 0
    last = 1e18
    #어떻게 하면 중복될떄를 방지할 수 있을까??
    ## 통과한 사람수가 n보다 많은 경우만 카운트 한다음 그중에 가장 작은 mid를 찾으면 되겠네!!!
    ## 범위가 중요하구나
    while last > first:
        mid = (first + last) // 2
        complete = sum(mid // time for time in times)
        if complete >= n:
            last = mid
            answer_list.append(mid)
        if complete < n:
            first = mid + 1

    return min(answer_list)


## 오류 해결용 커밋



print(solution(6,[10,10]))