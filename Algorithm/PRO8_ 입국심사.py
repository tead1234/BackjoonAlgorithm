def solution(n, times):
    ## n명이 줄을 서있을떄 가장 시간이 적게 걸리는 곳을 탐색한후 가면 되겠네
    ## 각 줄마다 걸리는 시간 - 경과시간  = 대기 시간 대기시간이랑 검사걸리는 시간을 더하면 걸리는 시간을 알 수있음
    # answer는 경과 시간
    # answer: int = 0
    # n = n - len(times)
    # wait = [0] * len(times)
    # save_times = times.copy()
    # c =0
    # while c != 1:
    #     answer += 1
    #
    #     for i in range(len(times)):
    #
    #         wait[i] = times[i] - answer
    #     for i in range(len(times)):
    #         if wait[i] == 0:
    #             times[i] += save_times[i]
    #             n -= 1
    #
    #         ## 문제가 0이 아닌곳에도 들어갈 수 있다는거
    #             ## wait가 0인곳은 이미 앞에서 업데이트됐음 근데 0이 아닌 곳들은 time가 업데이트가 안됐기때문에 answer를 빼면 더 적은 값음 나옴
    #             if n == 0:
    #                 for k in range(len(times)):
    #                     if wait[k] ==0 :
    #                         pass
    #                     else:
    #                         times[k] += save_times[k]
    #                     wait[k] = times[k] - answer
    #                 answer += min(wait)
    #                 c = 1
    ## 이분 탐색으로 접근 > 최소 걸리는 시간과 최대 시간을 예상
    start, last = 0, n * max(times)
    while start <= last:
        mid = (start+ last)// 2
        complete = sum(mid//time for time in times)
        if complete == n:
            return mid

        elif complete > n:
            last = mid

        elif complete < n:
            start  = mid








print(solution(6,[5,5,5,5]))