def NumberOfPaths(self,a, b):
        #code here
        if a == 1 or b == 1:
            return 1
        return self.NumberOfPaths(a-1,b)+self.NumberOfPaths(a,b-1)
