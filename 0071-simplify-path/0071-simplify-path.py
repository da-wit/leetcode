class Solution:
    def simplifyPath(self, path: str) -> str:        
        paths = path.split('/')
        stack = []
        for i in range(len(paths)):
            if paths[i] != "" and paths[i] != ".." and paths[i] != ".":
                stack.append(paths[i])
            elif paths[i] == ".." and stack:
                stack.pop()
        return "/"+ "/".join(stack)
        

        