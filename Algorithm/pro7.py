from collections import deque
T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    queue =deque()
    N, K = input().split()
    N = int(N)
    K = int(K)

    E=N/4
    list1 =[]
    list2 =[]
    list3 =[]
    list4 =[]
    a =""
    b =""
    c =""
    d =""
    list_sum = []
    number = input()
    number = list(number)
    for i in range(N):
        queue.append(number[i])
    ## 회전만 구현함녀 완료
    for _ in range(int(E)):
        if queue:
            v = queue.pop()
            queue.appendleft(v)
            for i in range(N):
                number[i] = queue[i]

        else:
            continue

        ## 이렇게 하면 자릿수를 넘어간느데 시발 ...
       ## 무식하게 여기서 슬라이싱 하자 E까지
        list1=number[0:int(E)]
        list3 = number[2*int(E): 3*int(E)]
        list2 = number[int(E):2*int(E)]
        list4 = number[3*int(E):4*int(E)]

        for i in range(len(list1)):
            a += list1[i]
        for i in range(len(list2)):
            b += list2[i]
        for i in range(len(list3)):
            c += list3[i]
        for i in range(len(list4)):
            d += list4[i]
        list_sum.append(int(a,16))
        a=""
        list_sum.append(int(b,16))
        b = ""
        list_sum.append(int(c,16))
        c = ""
        list_sum.append(int(d,16))
        d = ""


    list_sum2 = sorted(set(list_sum),reverse=True)
    print("#",test_case,"\t",list_sum2[K-1])

