class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=(len(height))-1
        MaxArea=0
        Value=0
        for i in range (len(height)):
            area = min(height[left],height[right])*(right-left)
            if (MaxArea<area):
                MaxArea=area
            if (height[left]<height[right]):
                left+=1
            elif(left==right):
                pass
            else:
                right-=1

        return MaxArea