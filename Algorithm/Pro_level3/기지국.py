def solution(n, stations, w):
    answer = 0

    check = [False] * n
    for s in stations:
        if s - 1 - w >= 0 and s - 1 + w < n:
            for k in range((s - 1 - w), (s + w)):
                check[k] = True
        elif s - 1 - w < 0 and s - 1 + w <= n:
            for k in range((s + w)):
                check[k] = True
        elif s - 1 - w >= 0 and s - 1 + w > n:
            for k in range((s - 1 - w), n):
                check[k] = True
    start = 0
    cnt = 0
    for idx1, ch in enumerate(check):
        if ch == False:
            start = idx1

            for idx2, ch2 in enumerate(check):
                if ch2 == False and start <= idx2:
                    cnt += 1
                    if cnt == w + 1:
                        answer += 1
                        if idx2 + w + 1 <= n:
                            for k in range(start, idx2 + w + 1):
                                check[k] = True
                                cnt = 0
                            break
                        elif idx2 + w + 1 :
                            for k in range(start, n):
                                check[k] = True
                                cnt = 0
                            break
                    elif idx2 == n-1:
                        answer += 1
                        for k in range(start, n):
                            check[k] = True
                elif ch2 == True and  start < idx2:
                    answer += 1
                    for k in range(start, idx2):
                        check[k] = True
                    cnt = 0
                    break
    print(answer)
    return answer
solution(6, [1,3,5], 1)