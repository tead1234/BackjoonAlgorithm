def getMaximumRemovals(order, source, target):
    # Write your code here
    ans = 0
    S = list(source)
    T = list(target)
    # 아마 반복문을 줄이거나 딕셔너리로 더 빠르게 만들수 이ㅏㅆ을거같은데
    if S == T:
        return 0
    for ord in order:
        flg2 = False
        S[ord-1] = "*"
        # T를 가지고 있는지 판단
        idx = -1
        ## 한 글자 씩 탐색
        for t in T:
            flg = False
            for i in range(idx,len(S)):
                if t == S[i] and i > idx:
                    flg = True
                    idx = i
                    break
                else:
                    continue
            if flg:
                continue
            if flg == False:
                flg2 = True
                break
        if flg2:
            return ans
        elif flg2 == False:
            ans += 1
    return ans

print(getMaximumRemovals([7,
1,
2,
5,
4,
3,
6],"ABBABAA","BB"))