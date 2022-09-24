from typing import List


def solution(k: int, dic: List[str], chat: str) -> str:
    answer = ''
    b = 0
    CHAT = chat.split()
    ## 완전일치 구분
    for c in range(len(CHAT)):
        if CHAT[c] in dic:
            CHAT[c] = '#' * len(CHAT[c])
    ## 일부일치 판단 >>
    for C in CHAT:
        stack = []
        flag = True
        for di in dic:
            if '#' in C:
                continue
            for s in range(len(C)):
                if C[s].isalpha():
                    leng = len(stack)
                    for i in range(len(di)):
                        if di[i] == C[s]:
                            if i <= leng * 3:
                                stack = []
                                flag = True
                                continue
                            else:
                                flag = False
                                stack = []
                                break
                    if flag:
                        for i,a in enumerate(CHAT):
                            if a == C:
                                o = i
                                CHAT[o] ='#' * len(di)

            # print(stripingC)
            # ## 일단 가능성있는 후보를 가져와
            # for D in range(len(CHAT)):
            #     stack = []
            #     ## 소문자를 가지고 있다면 되는지 안되는지 테스트
            #     ## 스택써서 .을 스택에 넣고
            #     if stripingC in CHAT[D]:
            #         for v in range(len(str(C)):
            #             if C[v] == '.':
            #                 stack.append(s)
            #             else:

    for ch in CHAT:
        answer += ch
        answer += " "
    return answer
print(solution(2, ["slang", "badword"], "badword ab.cd bad.ord .word sl.. bad.word"))