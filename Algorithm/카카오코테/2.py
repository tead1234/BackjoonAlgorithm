## cap 보다 deliveries를 몇번만에 끝낼 수 있는가
def solution(cap, n, deliveries, pickups):
    answer = 0
    CAP = cap
    k = n-1
    def find(CAP,k):

        while CAP > 0 or 0 not in deliveries:
            ## 딜리버리
            if CAP >= deliveries[k] and deliveries[k] > 0:
                CAP -= deliveries[k]
                deliveries[k] = 0
                k -= 1
                find(CAP,k)
                return
            elif CAP < deliveries[k] and deliveries[k] > 0:
                deliveries[k] -= CAP
                CAP  = 0
                return
            else:
                k -= 1
                print(deliveries)
        return

    while max(deliveries) != 0 or max(pickups) != 0:

        ## 딜리버리
        for i in range(len(deliveries)-1,0,-1):
            if deliveries[i] != 0:
                k = i
                break
        # answer += ((k + 1) * 2)

        find(CAP,k)
        answer += ((k+1)*2)
        CAP = cap
        print(answer)
            # if CAP > deliveries[v]:
            #     CAP -= deliveries[v]
            #     deliveries[v] = 0
            # else:
            #     cap = 0
            #     deliveries[v] -= CAP
            ## 수거

    return answer
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))