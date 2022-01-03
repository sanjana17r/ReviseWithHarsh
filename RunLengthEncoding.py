def encode(arr):
    count = 1
    res = ''
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            res+=(arr[i-1]+str(count))
            count = 1
        else:
            count+=1
    res+=(arr[-1]+str(count))
    return res
