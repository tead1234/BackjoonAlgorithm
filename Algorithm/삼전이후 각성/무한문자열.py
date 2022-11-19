import re
def match(a,b):
    # a가 더 길이가 작을때
    for i in range(len(a)):
        if a[i] != b[i]:
           	return False
    return True
T = int(input())
for test_case in range(1, T + 1):
    a= input().split()
    # print(type(a[0]))


    # print(match("ab","c"))
    answer = True
    a_first = a[0]
    a_sec = a[1]
    while len(a_first) != 0 and len(a_sec) != 0:
        if len(a_first) >= len(a_sec):
            flg = True

            if match(a_sec,a_first ):
                a_first = a_first[len(a_sec):]
                a_first , a_sec = a_sec, a_first

            else:
                flg = False
                break

        if len(a_first) < len(a_sec):
            flg = True
            if match(a_first,a_sec):
                a_sec = a_sec[len(a_first):]
                a_first, a_sec = a_sec, a_first

            else:
                flg = False
                break






    if flg:
        answer = "yes"
    else:
        answer = "no"



    print("#{} {}".format(test_case, answer))

