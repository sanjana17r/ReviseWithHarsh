def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1:
            return str2
        if not str2:
            return str1
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        elif str1[: len(str2)] == str2: #check if the starting of the str1 is = str2
            return self.gcdOfStrings(str1[len(str2) :], str2)
        else:
            return ''
        
