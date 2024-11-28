class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        # for i in nums1:
        #     if (i in nums2):
        #         result.append(i)
        #         nums2.remove(i)
        # a =defaultdict(int)
        # b=defaultdict(int)
        # for i in nums1:
        #     a[i]+=1
        # for j in nums2:
        #     b[j]+=1
        # for k,v in a.items():
        #     if k in b:
        #         res = [k] * min(a[k],b[k])
        #         result +=res
        # return result
                    

        nums1.sort()
        nums2.sort()
        if len(nums1)>=len(nums2) :
            l =0 
            r =0
            while r < len(nums1) and l < len(nums2):
                if nums1[r] == nums2[l]:
                    result.append(nums2[l])
                    l+=1
                    r+=1
                elif nums1[r] > nums2[l]:
                    l+=1
                else:
                    r+=1
        else:
            l=0
            r =0
            while r < len(nums2) and l < len(nums1):
                if nums2[r]==nums1[l]:
                    result.append(nums1[l])
                    l+=1
                    r+=1
                elif nums2[r] > nums1[l]:
                    l+=1
                else:
                    r+=1

        return result