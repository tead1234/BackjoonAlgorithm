from collections import deque
def de_3(num):
    sum =  0
    li = list(map(int,str(num)))
    for a in li:
        sum += a
    if sum % 3 == 0:
        return True
    return False

def de_10(num):
    li = deque(sorted(list(map(int, str(num)))))
    a = deque()
    answer = ''
    if 0 in li:
        while li:
            mix = li.popleft()
            a.appendleft(mix)
        a = list(map(str,a))
        for i in range(len(a)):
            answer += a[i]
        return answer

    elif 0 not in li:
        return False

num = int(input())
if num ==0:
    print(-1)
if de_3(num):
    if de_10(num) != False:
        print(de_10(num))
    else:
        print(-1)

print(-1)
