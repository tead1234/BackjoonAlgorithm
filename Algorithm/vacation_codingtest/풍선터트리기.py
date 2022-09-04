import heapq
def solution(a):
    answer = 0
    if len(a) < 3:
        answer = len(a)
    elif len(a) >= 3:
        answer = 2
        heapq.heapify(a[2:])
        q = []
        left = a[0]
        for bn in a[2:]:
            heapq.heappush(q,bn)
        right = heapq.heappop(q)
        for i in range(1, len(a) - 1):
            if right == a[i]:
                right = heapq.heappop(q)
                print(right)
                answer += 1
                continue
            if a[i] < left:
                answer += 1
                left = a[i]
                continue


    return answer


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))