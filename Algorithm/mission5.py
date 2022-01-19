list=[]
start = 0
def find_string(inputs):
    global start
    for i,k in enumerate(inputs):
        if k.isalpha() == True and inputs[i+1].isalpha() == False:
            list.append(inputs[start:i+1])

        else:
            start = i -1


    return list
inputs = "cqcqc14dfl513lo354o3"


print(find_string(inputs))