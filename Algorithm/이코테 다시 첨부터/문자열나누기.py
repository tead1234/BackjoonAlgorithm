def soultion(s):
    ans = []

    # s를 나누는 기준정하기
    last = ''
    idx = 0
    last = s[0]
    while idx < len(s)-1:
        # if s[idx] != s[idx+1]:
        #     last.join(s[idx])
        #     idx += 1

        i = 0
        while idx + i < len(s) and s[idx] == s[idx + i]:
            i += 1
        idx += i
        ans.append(s[:idx - i])
        ## 어디까지 점프할지 찾아야돼







    print( ans )

soultion('abvcaccaqrfq')
