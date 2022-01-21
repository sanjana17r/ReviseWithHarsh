def atoi(self,string):
        # Code here
        neg = 0
        res = 0
        i=0
        if string[0] == '-':
            neg = 1
            string = string[1:]
        while i<len(string):
            num = ord(string[i])-ord('0')
            if num>9 or num<0:
                return -1
            res = res*10+num
            i+=1
        if neg == 1:
            return -res
        return res
