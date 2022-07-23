def find(s, answer):
    if len(s) == 0:
        answer =1
        return answer
    else:
        for i in range(len(s) - 1):
            S= []
            S = s[i:i + 2]
            if S[0] == S[1]:
                del s[i:i + 2]
                s1 = s
                find(s1, answer)
                if len(s) == 0:
                    answer =1
                    return answer
                else:
                    answer =0
                    return answer
            else:
                continue
def solution(s):
    s = list(s)
    answer =0
    ans = find(s, answer)
    return ans
