class Solution:
    def simplifyPath(self, path: str) -> str:
        # x = path.split("/")
        
        x = path.split('/')
        stack = []
        # print(l)
        for i in range(1,len(x)):
            if x[i] != "" and x[i] != '..' and x[i] != '.':
                stack.append(x[i])
            else:
                if x[i] == '..':
                    if not stack:
                        pass
                    else:
                        stack.pop()
        return "/" + "/".join(stack)

        