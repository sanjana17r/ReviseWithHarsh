def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        dic = {}
        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        cur = 0
        for i in dic:
            if dic[i]>cur:
                cur = dic[i]
                ans = i
            elif dic[i]==cur:
                if i<ans:
                    cur = dic[i]
                    ans = i
        return [ans,dic[ans]]
