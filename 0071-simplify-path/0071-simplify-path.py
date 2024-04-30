class Solution:
    def simplifyPath(self, path: str) -> str:
        x = path.split("/")
        # print(x)
        stack = []
        for i in range(1,len(x)):
            if x[i] != "" and x[i] != ".." and x[i] != '.':
                stack.append(x[i])
           
            if x[i] =="..":
                if not stack:
                    pass
                else:
                    stack.pop()
        result = "/" + "/".join(stack)
        # print(stack)
        # print(result)
        return result

        