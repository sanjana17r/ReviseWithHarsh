def winnerOfGame(self, colors: str) -> bool:
        
        a,b=0,0
        for i in range(1,len(colors)-1):
            if colors[i]=='A' and colors[i-1] == 'A' and colors[i+1] == 'A':
                a+=1
            if colors[i]=='B' and colors[i-1] == 'B' and colors[i+1] == 'B':
                b+=1
        return a>b
