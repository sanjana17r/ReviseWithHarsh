def findPosition(self, N , M , K):
        # code here
        res = M+K-2
        res = res%N
        return res+1
