from collections import deque
def solution(s):
    answer = 0
    def isok(List):
        stack = []
        for s in List:
            if s == '(' :
                stack.append(s)
            elif s== '[':
                stack.append(s)
            elif s== '{':
                stack.append(s)


            elif s == ')' or ']' or '}':
                if len(stack) == 0:
                    return False
                last = stack.pop()
                elif s == ')' and last == "(":
                    continue
                elif s == ']' and last == "[":
                    continue
                elif s == '}' and last == "{":
                    continue
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
    S = list(s)
    S = deque(S)
    for _ in range(len(S)):
        S.append(S.popleft())
        if isok(list(S)):
            answer += 1
    return answer

print(solution("[{]}"))