from itertools import combinations


# 다트 한개로 만들수 있는 모든 점수를 찾아내고 대상점수를 맞
def solution(target):
    answer = []
    flg = False
    score_prime = [i for i in range(1, 21)] + [50]
    score_board = [i * j for i in range(1, 21) for j in range(1, 4)] + [50]
    k = 0
    k1 = target // 60
    k2 = target // 50
    target2 = target - k2 * 50
    target1 = target - k1 * 60

    for i in range(1, len(score_board)):
        a = list(combinations(score_board, i))
        for a_ in a:
            if sum(a_) == target2:
                cnt = 0
                for a_minus in a_:
                    if a_minus in score_prime:
                        cnt += 1
                if [len(a_) + k2, cnt] not in answer:
                    answer.append([len(a_) + k2, cnt + k2])
                    cnt = 0
                    flg = True
        if flg:
            break
    flg = False
    for i in range(1, len(score_board)):
        a = list(combinations(score_board, i))
        for a_ in a:
            if sum(a_) == target1:
                cnt = 0
                for a_minus in a_:
                    if a_minus in score_prime:
                        cnt += 1
                if [len(a_) + k1, cnt] not in answer:
                    answer.append([len(a_) + k1, cnt])
                    cnt = 0
                    flg = True
        if flg:
            break

    answer = sorted(answer, key=lambda x: (x[0], -x[1]))
    print(answer)
    return answer[0]

print(solution(167))
