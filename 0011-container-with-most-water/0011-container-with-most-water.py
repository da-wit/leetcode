class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) -1
        m = 0
        while left < right:
            
            # x = min(height[left],height[right])
            if height[left] < height[right]:
                x = height[left]
                m = max(m,x* (right -left))
                left +=1
            else:
                x = height[right]
                m = max(m, x *(right -left))
                right -=1
            
        return m

        


        return m