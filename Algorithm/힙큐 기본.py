import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while not scoville[0]>=K:
        if len(scoville) == 1:
            return -1
        heapq.heapify(scoville)
        first = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
        new_one = first + (sec*2)
        heapq.heappush(scoville, new_one)
        answer += 1
    return answer
## 정확성은 통과인데 효율성에서 막힘
print(solution([1, 2, 3, 9, 10, 12],7))