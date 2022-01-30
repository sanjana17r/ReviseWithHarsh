def power(self,x,y):
        #Your code here
        temp = 0
        if( y == 0):
            return 1
        temp = self.power(x, int(y / 2))
        if (y % 2 == 0):
            return (temp * temp)%1000000007
        else:
            return (x * temp * temp)%1000000007
