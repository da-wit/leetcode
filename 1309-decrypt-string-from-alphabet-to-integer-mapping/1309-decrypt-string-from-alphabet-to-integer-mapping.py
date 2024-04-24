class Solution:
    def freqAlphabets(self, s: str) -> str:
        val = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        y = {}
        for i in range(len(val)):
            y[str(i+1)] = val[i]
    
        # print(y)
        x = s.split('#')
        # print(x)
        z = ''
        right = 2
        i = 0
        while right < len(s):
            if s[right] == '#':
                z += y[s[i]+ s[i +1]]
                right +=3
                i +=3
            else:
                z+=y[s[i]]
                right +=1
                i +=1
        print(i,len(s))
        while i < len(s):
            z += y[s[i]]
            i+=1
        
        return z
        

