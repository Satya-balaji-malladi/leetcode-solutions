class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        data=[]
        for i in range(1,n+1):
            if (i%3==0 and i%5==0):
                data.append(str("FizzBuzz"))
            elif (i%3==0):
                data.append(str("Fizz"))
            elif(i%5==0):
                data.append(str("Buzz"))
            else:
                data.append(str(f"{i}"))
        return data

                