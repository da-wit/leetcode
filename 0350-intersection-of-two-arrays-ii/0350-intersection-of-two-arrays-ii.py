class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1 = [ ]
        i = 0
        while i <= len(nums1)-1:
            if nums1[i] in nums2:
                nums2.remove(nums1[i])
                list1.append(nums1[i])
                i +=1
            else:
                i += 1

        return list1