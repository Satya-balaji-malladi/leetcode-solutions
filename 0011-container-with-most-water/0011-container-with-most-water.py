class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=(len(height))-1
        MaxArea=0
        Value=0
        for i in range (len(height)):
            Value=self.MinValue(left,right,height)
            area = Value*(right-left)
            if (MaxArea<area):
                MaxArea=area
            if (height[left]<height[right]):
                left+=1
            elif(left==right):
                pass
            else:
                right-=1

        return MaxArea
    def MinValue(self,left,right,height):
        if (height[left]<height[right]):
            return height[left]
        else:
            return height[right]
