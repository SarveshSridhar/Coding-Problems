class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        stack = list()
        res = "/"
        # traversal
        for i in range(len(path_list)):
            # ignore "." and "" after splitting the absolute path
            if path_list[i] == '.' or path_list[i] == '':
                continue
            # go to previous directory if the current directory is not root (can be checked by seeing length of stack)
            if path_list[i] == '..':
                if len(stack) != 0:
                    stack.pop()
            # add the directories in path list
            else:
                stack.append(path_list[i])
        # make the canonical path
        for i in range(len(stack)):
            res += stack[i] + "/"
            print(res)
        # print canonical path
        # remove "/" in the end if we have directories --> "/home/dummy"
        # dont need to remove "/" in the end if we dont have directories --> "/"
        if len(res)>1:return res[:-1]
        return res
