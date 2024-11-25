class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d =defaultdict(int)
        
        left = 0
        m = 0

        for i in range(len(s)):
            
            d[s[i]] +=1 
            while d[s[i]] >1:
                d[s[left]] -=1
                if d[s[left]] == 0:
                    del[d[s[left]]]
                left +=1
            m = max(m,i - left +1)
        return m