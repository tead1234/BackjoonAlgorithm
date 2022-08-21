def solution(order):
    answer = 0
    container = [-1]
    stock = []
    key = 0
    last = 0
    for i in range(1, len(order)+ 1):
        stock.append(i)
    ## o는 무조건 넣어야 되는 물건
    for s in stock:
        ## 먼저 컨테이너에서 찾아보고
        ## 스탁에서 찾아보고
        ## 그래도 없으면 컨테이너로 계속 이동

        if len(container) != 0 and order[key] == container[last]:
            answer += 1
            key += 1
            container.remove(container[last])
        elif len(container) != 0 and order[key] == s:
            answer += 1
            key += 1
        else:
            container.append(s)
            last += 1

    for j in range(len(container)-1,0, -1):
        if container[j] != order[key]:
            break
        answer+= 1
        key += 1



    return answer
# print(solution([4,3,1,2,5]))
# print(solution([5,4,3,2,1\]))#
print(solution([1,2,3,4,5]))