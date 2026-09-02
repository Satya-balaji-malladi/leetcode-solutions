class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        MergedArray=nums1+nums2
        MergedArray=sorted(MergedArray)
        if ((len(MergedArray))%2==0):
            index=int(len(MergedArray)/2)
            value=((MergedArray[index]+MergedArray[index-1])/2)
            return value
        else:
            index=int((len(MergedArray)/2)-0.5)
            value=float(MergedArray[index])
            return value