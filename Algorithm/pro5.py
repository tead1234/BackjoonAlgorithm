def solution(numbers, target):
    global answer
    answer = 0
    N = len(numbers)
    global sum
    def dfs(a, numbers, sum, target):
        global answer
        if a == N  and sum == target:
                answer += 1
                return
        if a == N:
            return


        dfs(a+1 , numbers, sum+numbers[a], target)
        dfs(a+1 , numbers, sum-numbers[a], target)

    dfs(0, numbers,0,target)
    return answer
print(solution([1,1,1,1,1],3))

