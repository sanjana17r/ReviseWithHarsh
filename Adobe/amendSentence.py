def amendSentence(self, s):

        # code here
        string = ''
        ind = 0
        for i in range(1,len(s)):
            if s[i].isupper():
                string += (s[ind:i]+' ')
                ind = i
        string += s[ind:]
        string = string.lower()
        return string
