def solution(n, times):
    ## n명이 줄을 서있을떄 가장 시간이 적게 걸리는 곳을 탐색한후 가면 되겠네
    ## 각 줄마다 걸리는 시간 - 경과시간  = 대기 시간 대기시간이랑 검사걸리는 시간을 더하면 걸리는 시간을 알 수있음
    # answer는 경과 시간
    answer = 0
    n = n - len(times)
    wait = [0] * len(times)
    save_times = times.copy()
    while n != 0:
        answer += 1

        for i in range(len(times)):

            wait[i] = times[i] - answer
        for i in range(len(times)):
            if wait[i] == 0:
                times[i] += times[i]
                n -= 1
        if n == 1:
            for n,m in enumerate(wait):
                if m == 0:
                    answer += save_times[n]
            least = wait[0] + times[0]
            for k in range(len(times)):
                if wait[k] + times[k] <= least:
                    least = wait[k] + save_times[k]
            answer += least
            return answer

print(solution(6,[7,10,10,30]))