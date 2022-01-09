def matchPairs(self,nuts, bolts, n):
		# code here
        arr = ['0']*9
        for i in range(len(nuts)):
            if nuts[i] == '!':
                arr[0] = '!'
            elif nuts[i] == '#':
                arr[1] = '#'
            elif nuts[i] == '$':
                arr[2] = '$'
            elif nuts[i] == '%':
                arr[3] = '%'
            elif nuts[i] == '&':
                arr[4] = '&'
            elif nuts[i] == '*':
                arr[5] = '*'
            elif nuts[i] == '@':
                arr[6] = '@'
            elif nuts[i] == '^':
                arr[7] = '^'
            else:
                arr[8] = '~'
        count = 0
        for i in range(9):
            if arr[i]!='0':
                nuts[count] = arr[i]
                bolts[count] = arr[i]
                count+=1
