class Solution(object):
    def areNumbersAscending(self, s):
        minValue = 0
        isOk = True
        i =0
        size = len(s)
        while i < size:
            if s[i].isdigit():
                if(i+1>=size or  not s[i+1].isdigit()):
                    dig = int(s[i])
                    i+=1
                else:
                    dig = int(s[i]+s[i+1])
                    i+=2
                if dig>minValue:
                    minValue = dig
                else:
                    isOk = False
                    break    
            else:i+=1     
        return isOk

        