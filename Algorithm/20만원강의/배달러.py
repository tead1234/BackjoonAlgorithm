def solution(order):
    answer = 0
    container = [0]
    stock = []
    last = 0
    key = 0
    for i in range(1, len(order) + 1):
        stock.append(i)
    ## o는 무조건 넣어야 되는 물건
    for ord in order:
        if stock[key] == ord:
            answer += 1
            key += 1
        if ord == container[last]:
            answer += 1
            last -= 1
        else:
            container.append(stock[key])
            key += 1
            last += 1

    print(answer)
    print(container)
solution([4,3,1,2,5])
solution([5,4,3,2,1])