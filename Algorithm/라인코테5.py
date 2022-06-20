from collections import deque
짝수행렬 = []
홀수행렬 = []

arr = [7,6,8,9,10,3000,5151]
    ##[2,8,3,6,1,9,1,9]
k =0
def solution(arr, k):
    ## arr이 짝수개면 짝수번째 수와 홀수번째 수를 가져와서
## 두 수의 차이가 마이너스면 교환권을쓰고 플러스면 안쓰는걸로
## 만약에 교환권보다 마이너스인 경우가 더 많으면 마이너스가 더 큰 상태에서만 쓰기
    arr = sorted(arr, reverse=True)
    나머지행렬 = deque()

    answer = 0
    ## 짝수일경우만
    if len(arr) % 2 ==0:
        for i in range(len(arr)):
    # 여기선 i가 홀수여야지
            ## 실시간 판단해버리면 어떨때 교환권을 써야할지 애매함
            if i%2 == 0:
                홀수행렬.append(arr[i])
            if i %2 ==1:
                answer += arr[i]
                짝수행렬.append(arr[i])

        for i in range(len(짝수행렬)):
            나머지 = 홀수행렬[i] - 짝수행렬[i]
            if 나머지 > 0:
                나머지행렬.append(나머지)
        나머지행렬 = sorted(나머지행렬, reverse= False)
        if len(나머지행렬) > k:
            for k in range(k):
                # print(나머지행렬.pop())
                answer += 나머지행렬.pop()
        else:
            for k in range(len(나머지행렬)):
                # print(나머지행렬.pop())
                answer += 나머지행렬.pop()
            ## 올림차순정렬

        return answer
    ## 홀수일경우
    if len(arr) % 2 == 1:
        arr.append(0)
        for i in range(len(arr)):
            if i % 2 == 0:
                홀수행렬.append(arr[i])
            if i % 2 == 1:
                answer += arr[i]
                짝수행렬.append(arr[i])
        for i in range(len(짝수행렬)):
            나머지 = 홀수행렬[i] - 짝수행렬[i]

            if 나머지 > 0:
                나머지행렬.append(나머지)
        나머지행렬 = sorted(나머지행렬, reverse= False)
        if len(나머지행렬) > k:
            for _ in range(k):
                # print(나머지행렬.pop())
                answer += 나머지행렬.pop()
        else:
            for _ in range(len(나머지행렬)):
                # print(나머지행렬.pop())
                answer += 나머지행렬.pop()
            ## 올림차순정렬

        return answer
print(solution(arr,1))