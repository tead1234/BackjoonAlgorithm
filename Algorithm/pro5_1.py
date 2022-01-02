# test case 만 통과 ;
def solution(numbers, target):

    global answer
    answer = 0
    N = len(numbers)

    def dfs(idx, numbers, total):
        global answer
        if (idx == N) and (total == target):
            answer += 1
            return
        if idx == N:
            return

        dfs(idx + 1, numbers, total + numbers[0])
        dfs(idx + 1, numbers, total - numbers[0])

    dfs(0, numbers, 0)

    return answer

print(solution([1,1,1,1,1],3))