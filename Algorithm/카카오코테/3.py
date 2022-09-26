from itertools import permutations


## dlahxlszhs vmffjtmfmf chleo
# 그다음 이모티콘 판매가격 최대
def dfs(start):
    visited[emoticons.index(start)] = 1
    mu = [40, 30, 20, 10]
    for k in range(4):
        if visited[emoticons] == 0:
            start = (start // 100) * mu[k]
            answer.append(start)
            dfs()


def solution(users, emoticons):
    visited = [0] * len(emoticons)
    answer = []
    mu = [40, 30, 20, 10]
    v = 0
    k = 0
    total = 0
    muList = list(permutations(mu, len(emoticons)))

    # 프리미엄 가입
    TOTAL = 0
    nopre = 0
    TOTALLIST = 0
    V = []
    for m in muList:
        for user in users:
            rate, val = user
            for k in range(len(m)):
                if m[k] >= rate:
                    v = (emoticons[k] // 100) * (100 -m[k])
                    total += v

            if total > val:

                TOTAL += 1
                total = 0

            else:
                nopre += total
                total = 0
                if nopre == 14000:
                    print(m)

        answer.append([TOTAL,nopre])
        TOTAL = 0
        nopre = 0
    print(answer)

    return max(answer)
print(solution(
[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))