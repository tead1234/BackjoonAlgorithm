li = list(map(int,input().split()))
up = 0
down = 0
mx_up = 0
mx_down = 0
for i in range(len(li)):
    if i == len(li) - 1:
        if li[i] > li[i-1]:
            up += 1
            break
        elif li[i] < li[i-1]:
            down += 1
            break
        else:
            break
    if li[i] < li[i+1]:
        up += 1
        mx_down = down
        down = 0
    elif li[i] > li[i+1]:
        down += 1
        mx_up = up
        up=0
    elif li[i] == li[i+1]:
        if i == 0:
            continue
        else:
            if li[i-1] < li[i]:
                up += 1
                mx_up = up
            if li[i-1] > li[i]:
                down += 1
                mx_down = down

if mx_up < up:
    mx_up = up
elif mx_down < down:
    mx_down = down

if mx_up <= 2:
    mx_up = 1
if mx_down <= 2:
    mx_down = 1
print(mx_up,mx_down)
