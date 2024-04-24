class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        for i in range(len(words)):
            words[i] = list(words[i])
        print(words)
        x = []
        for i in range(len(words[0])):
            y = []
            for j in range(1,len(words)):
                if words[0][i] in words[j]:
                    if words[0][i] not in y:
                        y.append(words[0][i])
                    words[j].remove(words[0][i])
                else:
                    if words[0][i] in y:
                        y.remove(words[0][i])
                    break
            x.extend(y)
        
        print(x)
        return x

                    
               

            
        