def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []

    for idx, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(idx)

    return answer
## stack을 이용한 시간 단축