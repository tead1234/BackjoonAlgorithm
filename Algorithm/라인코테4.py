def solution(arr=[],brr=[]):
    answer = 0
    for i in range(len(arr)-1):
        나머지 = arr[i] - brr[i]
        arr[i+1] = arr[i+1] + 나머지
        if 나머지 == 0 :
            continue
        else:
            answer +=1

    return answer



print(solution([3,7,2,4],[13,1,1,1]))