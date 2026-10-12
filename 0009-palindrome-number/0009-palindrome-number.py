class Solution:
    def isPalindrome(self, x: int) -> bool:
        revNumber=0
        dupNumber=x
        if (x==0):
            return True
        if (x>0):
            while (x>0):
                remainder=x % 10
                revNumber=(revNumber*10)+remainder
                x=x//10
        if revNumber < -(2**31) or revNumber > 2**31 - 1:
            return False
        if (dupNumber==revNumber):
            return True
        else:
            return False
            
