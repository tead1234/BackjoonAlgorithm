
def solution(scores):
    answer = -1
    idx = 1
    start = 0
    new = []
    ## score
    wanho = [sum(scores[0]), scores[0][0], scores[0][1]]
    for sc in scores:
        new.append([sum(sc), sc[0], sc[1]])
    new.sort(key = lambda x : (-x[0], -x[1], -x[2]))
    for n in new:
        a,b,c = n
        if a != start:
            idx += 1
            start = a
            
            
    print(new)
    return answer