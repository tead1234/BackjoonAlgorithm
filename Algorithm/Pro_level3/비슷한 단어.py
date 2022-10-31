N = int(input())
LIST = [list(input()) for _ in range(N)]
KEY = LIST[0]
LIST= LIST[1:]
ans = 0

def compare(A,B):

    dic_A = {}
    dic_B = {}
    for a in A:
        if a not in dic_A.keys():
            dic_A[a] = 1
        else:
            dic_A[a] += 1
    for b in B:
        if b not in dic_B.keys():
            dic_B[b] = 1
        else:
            dic_B[b] += 1
    a = [i for i in dic_A.keys() if i not in dic_B.keys()]
    b = [i for i in dic_B.keys() if i not in dic_A.keys()]
    ## 서로 다른 키값으 가지고 그 갯수가 같을경우
    if len(a) == len(b) == 1:
        if dic_A[a[0]] == dic_B[b[0]]:
            same = [x for x in dic_A.keys() if x in dic_B.keys()]
            for s in same:
                if abs(dic_A[s] - dic_B[s])  != 0 :
                    return False
                elif abs(dic_A[s] - dic_B[s]) == 0:
                    continue
            return True
    # 같은키인데 각 갯수만 다른경우
    elif len(a) == len(b) == 0:
        cnt = 0
        same = [x for x in dic_A.keys() if x in dic_B.keys()]
        for s in same:
            if abs(dic_A[s] - dic_B[s]) > 1:
                return False
            elif abs(dic_A[s] - dic_B[s]) == 1:
                cnt += 1
        if cnt > 2:
            return False

        return True

    elif (len(a) == 1 and len(b) == 0) or (len(a)== 0 and len(b) == 1):
        cnt = 0
        if len(a) == 1 and dic_A[a[0]] == 1:
            same = [x for x in dic_A.keys() if x in dic_B.keys()]
            for s in same:
                if abs(dic_A[s] - dic_B[s]) == 1:
                    cnt += 1
                elif abs(dic_A[s] - dic_B[s]) > 1:
                    return False
                elif abs(dic_A[s] - dic_B[s]) == 0:
                    continue
            if cnt > 1:
                return False
            elif cnt == 0 :
                return False
            elif cnt ==1 :
                return True
        elif len(b) == 1 and dic_B[b[0]] == 1:
            same = [x for x in dic_A.keys() if x in dic_B.keys()]
            for s in same:
                if abs(dic_A[s] - dic_B[s]) == 1:
                    cnt += 1
                elif abs(dic_A[s] - dic_B[s]) > 1:
                    return False
                elif abs(dic_A[s] - dic_B[s]) == 0:
                    continue
            if cnt > 1:
                return False
            elif cnt == 0:
                return False
            elif cnt == 1:
                return True
        ## 남는 키값의 값이 1이고 그걸
        return False


def insert(A,B):
    dic_A = {}
    dic_B = {}
    cnt = 0
    for a in A:
        if a not in dic_A.keys():
            dic_A[a] = 1
        else:
            dic_A[a] += 1
    for b in B:
        if b not in dic_B.keys():
            dic_B[b] = 1
        else:
            dic_B[b] += 1
    a = [i for i in dic_A.keys() if i not in dic_B.keys()]
    b = [i for i in dic_B.keys() if i not in dic_A.keys()]
    same = [x for x in dic_A.keys() if x in dic_B.keys()]

    ## sanekey byt val different
    if len(a) == len(b) == 0:
        for s in same:
            if abs(dic_A[s] - dic_B[s]) == 1:
                cnt += 1
            elif abs(dic_A[s] - dic_B[s]) > 1:
                return False
        if cnt >1:
            return False

        return True

    elif (len(a) == 1 and len(b) == 0) or (len(a)== 0 and len(b) == 1):

        if len(a) == 1:
            if dic_A[a[0]] ==1:
                for s in same:
                    if dic_B[s] != dic_A[s]:
                        return False
        elif len(b) == 1:
            if dic_B[b[0]] == 1:
                for s in same:
                    if dic_B[s] != dic_A[s]:
                        return False
        return True

# 각 단어 뻉호가
for WORD in LIST:
    ## 길이가 같으면 단어 치환 or 같은 단어
    if len(WORD) == len(KEY):

        if compare(WORD,KEY):
            ans += 1

    elif abs(len(WORD) - len(KEY)) == 1:

        if insert(WORD,KEY):

            ans += 1

print(ans)




