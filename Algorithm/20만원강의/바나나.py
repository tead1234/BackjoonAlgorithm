def solution(want, number, discount):
    answer = 0
    dic = {}
    dicForwant = {}
    for a, b in zip(want, number):
        dicForwant[a] = b
    l = len(discount)
    copy = discount[0: 10]
    for a in copy:
        if a in dic.keys():
            dic[a] += 1
        else:
            dic[a] = 1
    A = len(list(dicForwant.items()) + list(dic.items()))
    B = len(set(list(dicForwant.items()) + list(dic.items())))
    C = len(dicForwant.items())
    if A - B == C:
        answer += 1
    for i in range(1, l):
        if i + 9 >= l:
            break
        else:
            ## 배열 머리에 있는 애를 제외
            ## 배열에 추가된 애를 추가 시키기
            ## 배열에 없던애 였으면 신규 생성
            ## 사전에 있던애의 값이 0이 되면 제거
            if discount[i + 9] not in dic.keys():
                dic[discount[i + 9]] = 1
                dic[discount[i - 1]] -= 1
                if dic[discount[i - 1]] == 0:
                    del dic[discount[i - 1]]
            else:
                dic[discount[i + 9]] += 1
                dic[discount[i - 1]] -= 1
                if dic[discount[i - 1]] == 0:
                    del dic[discount[i - 1]]
            A = len(list(dicForwant.items()) + list(dic.items()))
            B = len(set(list(dicForwant.items()) + list(dic.items())))
            if A - B == C:
                answer += 1

    return answer