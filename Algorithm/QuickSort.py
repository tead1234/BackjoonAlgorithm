arr = [1,4,5,16,6,47,37,31]

def Quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return Quick(left) + [pivot] + Quick(right)

print(Quick(arr))
num_arr = []
N = int(input())
for i in range(N):
    num_arr.append(int(input()))
def reverseQuick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    list = arr[1:]

    left = [x for x in list if x > pivot]
    right = [x for x in list if x <= pivot]

    return reverseQuick(left) + [pivot] + reverseQuick(right)



print(reverseQuick(num_arr))