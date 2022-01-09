def colName (self, n):
        # your code here
        string = ""
        while(n>0):
            rem = n%26
            if(rem==0):
                string+='Z'
                n = int(n/26)-1
            else:
                string+=chr((rem-1)+ord('A'))
                n = int(n/26)
        return(string[::-1])
