
def solution(participant, completion):
    answer = ""
    for part in participant:
        if part not in completion:
            answer = part
            break
        if part in completion:
            completion.remove(part)
    ## 중복찾기 알고리즘
    return answer

def solution(participant, completion):
    d = dict()
    for p in participant:
        d[p] = d.get(p, 0) + 1
    for c in completion:
        d[c] -= 1
        if d[c] == 0:
            del d[c]
    return list(d.keys()).pop()
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
