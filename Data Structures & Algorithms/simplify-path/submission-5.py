class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        split_path = path.split("/")

        for p in split_path:
            if p == "" or p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        
        return "/" + "/".join(stack)