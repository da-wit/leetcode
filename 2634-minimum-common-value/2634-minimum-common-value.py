class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        n = set(nums1)
        m = set(nums2)
        l = float('inf')
        for i in n:
            if i in m:
                l = min(l,i)
        
        if l != float('inf'):
            return l
        else:
            return -1


