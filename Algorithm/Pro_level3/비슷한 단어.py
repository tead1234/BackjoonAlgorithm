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
    if len(a) == len(b) == 1:
        if dic_A[a[0]] == dic_B[b[0]]:
            return True
    if len(a) == len(b) == 0:
        return True
    else:
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
    ## sanekey byt val different
    if len(a) == len(b) == 0:
        for i in range(len(dic_A.values())):
            if list(dic_A.values())[i] != list(dic_B.values())[i]:
                cnt += 1
            if cnt >1:
                return False

        return True

    elif (len(a) == 1 and len(b) == 0) or (len(a)== 0 and len(b) == 1):
        if len(a) == 1:
            if dic_A[a[0]] ==1:
                return True
        elif len(b) == 1:
            if dic_B[b[0]] == 1:
                return True
    return False

# 각 단어 뻉호가
for WORD in LIST:
    ## 길이가 같으면 단어 치환 or 같은 단어
    if len(WORD) == len(KEY):

        if compare(WORD,KEY):
            print(WORD)
            ans += 1

    elif abs(len(WORD) - len(KEY)) == 1:

        if insert(WORD,KEY):
            print(WORD)

            ans += 1

print(ans)




