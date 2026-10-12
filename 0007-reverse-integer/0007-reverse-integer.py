class Solution:
    def reverse(self, x: int) -> int:
        revNumber=0
        if (x==0):
            return 0
        if (x>0):
            while (x>0):
                remainder=x % 10
                revNumber=(revNumber*10)+remainder
                x=x//10
        elif x<0 :
            x=abs(x)
            while (x>0):
                remainder=x % 10
                revNumber=(revNumber*10)+remainder
                x=x//10
            revNumber=-revNumber
        if revNumber < -(2**31) or revNumber > 2**31 - 1:
            return 0


        return revNumber