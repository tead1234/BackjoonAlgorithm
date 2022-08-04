n = int(input())
def draw(n):
    if n == 3:
        print("*" * 3)
        print("*"+" "+"*")
        print("*" * 3)

    else:
        draw(n//3)


draw(n)