def solution(scoville, K):
    answer = 0
    mini = min(scoville)
    if mini >= K:
        answer = 0
    while mini < K and len(scoville) != 1:
        a = mini
        scoville.remove(a)
        b = min(scoville)
        scoville.remove(b)
        c = a + (b *2)
        scoville.append(c)
        mini = min(scoville)
        answer += 1
    if len(scoville) == 1:
        answer = -1
    return answer

print(solution([1, 2, 1,1, 10, 0],7))