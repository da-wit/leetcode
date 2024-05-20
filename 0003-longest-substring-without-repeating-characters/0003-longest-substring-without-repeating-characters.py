class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        x = defaultdict(int)
        left = 0
        for right in range(len(s)):
            x[s[right]] +=1
            
               
            

            while x[s[right]] > 1:
                
                x[s[left]] -=1
                if x[s[left]] == 0:
                    del x[s[left]]
                left +=1
            
            m = max(m,right - left + 1)
        return m
                










        # x = list(map(str,s))
        # y = []
        # z,m= 0,0
        # i =0
        # while i < len(x):
        #     if x[i] not in y:
        #         y.append(x[i])
        #         z+=1
        #         m = max(m,z)
        #         i+=1
        #     else:
        #         y.pop(0)
        #         z-=1
        # return m
                

    
            


        # x = {}
        # left = 0
        # max_substring = 0
        # if s  == " ":
        #     return 1

        # for right in range(len(s)): 
        #     if s[right] not in x:
        #         x[s[right]] = 1
        #     else:
        #         x[s[right]] += 1
        #     while x[s[right]] >= 2:
        #         max_substring = max(max_substring,right-left)
        #         x[s[left]] -= 1
        #         left += 1

        # return max_substring
        # d = {}
        # left = 0
        # for i in range(len(s)):
        #     if s[i] not in x:
        #         d[s[i]] = 1
        #     else:
        #         d[s[i]] +=1

        #     while d[s[i]] > 1:
                

