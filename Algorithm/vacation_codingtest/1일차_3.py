from collections import deque
s = deque(list(input()))
max_val = 0
while len(s) != 1:
    a = s.popleft()
    b = s.popleft()
    if a == '0' or a == '1' or b == '0' or b =='1':
        s.appendleft(str(int(a)+int(b)))
    else:
        s.appendleft(str(int(a) * int(b)))
print(s.popleft())