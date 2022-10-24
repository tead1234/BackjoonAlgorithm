def solution(play_list, listen_time):
    answer = 0
    List = [0] * sum(play_list)
    k = 0
    if sum(play_list) <= listen_time:
        answer = len(play_list)
        return answer
    for idx, music in enumerate(play_list):

        for n in range(k, music + k):
            List[n] = idx
        k += music
    k1 = len(List)
    List *= 2
    for j in range(k1 + 1):

        s = len(set(List[j:j + listen_time]))
        if s > answer:
            answer = s
    return answer


print(solution([10, 200, 30, 40], 6000))