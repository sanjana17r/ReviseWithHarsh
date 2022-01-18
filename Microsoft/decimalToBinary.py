def convert(num):
    x = ''
    while num>1:
        r = num%2
        if r == 1:
            x+='1'
        elif r==0:
            x+='0'
        num = num//2
    x+='1'
    x = x[::-1]
    return x
def generate(N):
    # code here
    res = []
    for i in range(1,N+1):
        res.append(convert(i))
    return res
