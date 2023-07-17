def solution(scores):
    answer = -1
    idx = 0
    stack = 1
    wonho = sum(scores[0])
    check_score = 999999999
    ## 가장 최고 점수를 가진 애들로만 따져도 되지 않을까???
    new = []
    chekingL = []
    chekingKey = []
    Id = 0
    for score in scores:
        if wonho < sum(score):
            new.append([score[0], score[1], Id])
            Id += 1
    new.sort(key=lambda x: (-x[0], -x[1]))

    F = False
    for new_idx, n in enumerate(new.copy()):

        a, b, c = n
        if a not in chekingKey:
            chekingKey.append(a)
            chekingL.append([a, b])

        if F:
            break
        ## 위 단계를 넘어가면
        if a < check_score:
            idx += stack
            stack = 1
            check_score = a
        elif a == check_score:
            stack += 1
        if d == 0:
            answer = idx
            F = True
        # print(idx, stack)
    return answer