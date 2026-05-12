class Solution(object):
    def strongPasswordCheckerII(self, password):
        isHaveDigit ,lower,upper,special=False,False,False,False
        lenPass = len(password)
        if(lenPass>=8 and lenPass<=100):
            for i in range(lenPass):
                if(isHaveDigit == False and password[i].isdigit()):isHaveDigit = True
                elif(lower == False and password[i].islower()):lower = True
                elif(upper == False and password[i].isupper()):upper = True
                elif(special == False and not password[i].isalnum()):special = True
                if(i<lenPass-1 and password[i] == password[i+1]):
                    return False
            return isHaveDigit and lower and upper and special
        else:
            return False
        