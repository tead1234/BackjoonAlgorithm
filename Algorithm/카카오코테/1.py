
def solution(today, terms, privacies):
    ## 프라이버시에서 하나씩 가져온다음  유효기간 계산하고 유혀한지 안한지 파악
    ## 달만큼 더하고 일에서 -1을하는데 dd 가 01이면 28로 넘어감
    dic = {}
    answer = []
    TODAY = today.split('.')
    k = 0
    for t in terms:
        약관,기간 = t.split()
        if 약관 not in dic.keys():
            dic[약관] = 기간
    for pr in privacies:
        k += 1
        # 분해하기
        y,m,U = pr.split(".")
        d,약관 = U.split()
        add = int(dic[약관])
        y = int(y)
        if m[0] == '0':
            m = int(m)
        else:
            m = int(m)
        y += add+m//12
        m += add %12

        if d[0] == '0':
            d = int(d[1])
        else:
            d = int(d)
        if m >12:
            m -= 12




        if d == 28:
            d -= 1
        elif d == 1:
            d = 28
            m -= 1
            if m == 0:
                m = 12
                y -= 1
        else:
            d -= 1
        print(y,m,d)

        Y,M,D = TODAY
        if D[0] == 0:
            D = D[1]
        if int(Y) > y:
            answer.append(k)

        elif int(Y) == y:
            if int(M) > m:
                answer.append(k)
            elif int(M) == m:
                if int(D) >= d:
                    answer.append(k)

    return answer

solution(
"2020.01.01", ["Z 3", "D 12"], ["2019.12.28 D"])