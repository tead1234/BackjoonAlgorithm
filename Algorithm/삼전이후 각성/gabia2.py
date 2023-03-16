from collections import deque


def solution(N, coffee_times):
    answer = []
    ## 그냥 단순 구현인가?
    # 커피에다가 순서표를 달고
    ## 가장 적은 시간이 남은 애부터 빼기
    ## 최종적으로 더 들어갈 커피가 ㅇ벗으면 남은 시간 순서로 넣기
    coffee = []
    for idx, co in enumerate(coffee_times):
        coffee_times[idx] = (idx + 1, co)
    q = deque(coffee_times)
    while q:
        if len(coffee) < N:
            coffee.append(q.popleft())
        elif len(coffee) == N:
            ## 가장 적은 시간이 남은 애 찾기
            print(coffee)
            coffee = sorted(coffee, key=lambda x: x[1])
            최소 = coffee[0][1]
            for i in range(len(coffee)):
                a, b = coffee[i]
                if b - 최소 == 0:
                    answer.append(a)

                else:
                    coffee[i] = (a, b - 최소)
            for c in coffee:
                c_inx, c_time = c
                if c_time == 0:
                    coffee.remove(c)
    return answer

print(solution(3, [4,2,2,5,3]))