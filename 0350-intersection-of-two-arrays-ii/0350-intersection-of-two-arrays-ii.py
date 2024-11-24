class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        # for i in nums1:
        #     if (i in nums2):
        #         result.append(i)
        #         nums2.remove(i)
        l = 0
        r = 0
        while l<len(nums1) and r < len(nums2):
            if(len(nums1)>=len(nums2)):
                if (nums1[l] == nums2[r]):
                    result.append(nums1[l])
                    l+=1
                    r+=1
                else:
                    l+=1
            else:
                if (nums1[l] == nums2[r]):
                    result.append(nums1[l])
                    l+=1
                    r+=1
                else:
                    r+=1


        return result