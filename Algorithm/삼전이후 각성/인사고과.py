def solution(scores):
    answer = -1
    idx = 1
    new = []
    check = []
    flg = 0
    ## score
    wanho = [sum(scores[0]), scores[0][0], scores[0][1]]
    for sc in scores:
        new.append([sum(sc), sc[0], sc[1]])
    new.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    check.append([new[0][1], new[0][2]])
    # print("수행")
    flg = sum(new[0])
    for n in new:
        a, b, c = n
        # print(a,b,c)
        if a < flg:
            if a == wanho[0]:
                out = False
                for m in check:
                    if m[0] > b and m[1] > c:
                        out = True
                        break
                if out:
                    answer = -1
                    return answer
                else:
                    answer = idx
                    return answer

            else:
                out = False
                for m in check:
                    # print(check)
                    if m[0] > b and m[1] > c:
                        out = True
                        break
                if out:
                    continue
                else:
                    check.append([b, c])
                    idx += 1
                    flg = a
        elif a == flg:

            idx += 1