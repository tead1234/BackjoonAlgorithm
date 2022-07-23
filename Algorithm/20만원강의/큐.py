from collections import deque

stack = deque()
cnt = 1
n = int(input())
while True:
    명령 = input().split()
    cnt += 1
    if 명령[0] == "push":
        stack.append(명령[1])
    elif 명령[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 명령[0] == "front":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    elif 명령[0] == "back":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])
    elif 명령[0] == "size":
        print(len(stack))
    elif 명령[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.popleft())
    elif n == cnt:
        break
