N = int(input())
def findSquare(List):
    List = sorted(List)
    x,y = List[0]
    z,w = List[3]
    k,o = List[1]
    b,u = List[2]
    if z-x == 1 and w-y == 1:
        if k-b == -1 and u-o == -1:
            return True
    return False

def makeDragon(x,y,d,g):
    dragon = []
    k = 0
    dragon.append((x,y))
    if d == 0:
        dragon.append((x+1, y))
    elif d== 1:
        dragon.append((x, y-1))
    elif d == 2:
        dragon.append((x-1, y))
    else:
        dragon.append((x, y+1))

    while k!= g:
        dragonCopy = dragon.copy()
        last = dragon.pop()
        moveX, moveY = last
        for i in range(len(dragon)-1,-1,-1):
            draX, draY = dragon[i]
            draX -= moveX
            draY -= moveY
            draX, draY = draY * -1, draX
            draX += moveX
            draY += moveY
            dragonCopy.append((draX,draY))
        dragon = dragonCopy
        k += 1
    return dragon

ans = []
passed = []
for _ in range(N):
    x,y,d,g = map(int,input().split())
    List1 = makeDragon(x,y,d,g)
    for l in List1:
        if l not in ans:
            ans.append(l)

ANSWER = 0
for A in ans:
    a,b = A
    ## 아래점
    if (a,b+1) in ans:
        ## 오른쪽점
        if (a+1,b) in ans:
            #대각
            if (a+1,b+1) in ans:
                ANSWER +=1

print(ANSWER)