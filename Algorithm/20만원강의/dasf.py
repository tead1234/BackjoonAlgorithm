def solution(order):
    answer = 0
    container = []
    stock = []
    last = 0
    flag = True
    for i in range(1, len(order)+ 1):
        stock.append(i)
    ## o는 무조건 넣어야 되는 물건
    for o in order:

        while len(stock) != 0:
            c = stock[0]
            if o != c:
                if len(container) == 0:
                    container.append(c)
                    stock.remove(c)
                    continue
                elif o == container[last]:
                     answer += 1
                     container.remove(container[last])
                     last -= 1
                     continue
                elif o != container[last]:
                    container.append(c)
                    last += 1
                    stock.remove(c)
                    continue
            else:
                answer += 1
                stock.remove(c)

        if container[last] == o:
            answer += 1
            last -= 1
            continue



    return answer
print(solution([4,3,1,2,5]))
print(solution([5,4,3,2,1]))