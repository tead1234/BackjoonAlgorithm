from collections import deque
def slice(s,k):
    b= [s[i:i+k] for i in range(0,len(s),k)]
    return b
def count(s):
    front = 0
    c = []
    s = deque(s)
    key = ""
    for i in range(len(s)):
        if key == s[i]:
            continue
        key = s[i]
        for j in range(i+1,len(s)):

            if key == s[j]:
                front += 1


            elif s[i] != s[j]:
                break
        if front == 0:
            c.append(key)
            continue
        elif front > 0:
            c.append(front+1)
            c.append(key)

        front = 0
    return c
def solution(s):
    key = 999999
    if len(s) <=1:
        key = len(s)
        return key
    for i in range(1,len(s)-1):
        sliced_S = slice(s,i)
        Counted_S = count(sliced_S)
        sens = "".join(map(str,Counted_S))
        if key > len(sens):
            key = len(sens)
    return key



print(solution("abcabcdede"))