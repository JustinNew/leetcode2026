# 71. Simplify Path
# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
# In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.
# The canonical path should have the following format:
# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.
# The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
# Return the simplified canonical path.

# Key is to use a stack to store the simplified path.
# Then, iterate through the path and add the directories to the stack.
# If the directory is '.', continue.
# If the directory is '..', pop the last directory from the stack.
# Otherwise, add the directory to the stack.
# Finally, return the simplified path.

# example:
# Input: path = "/home/"
# Output: "/home"

# example:
# Input: path = "/../"
# Output: "/"

# example:
# Input: path = "/home//foo/"
class Solution:
    def simplifyPath(self, path: str) -> str:
        root = path.split('/')
        root = [s for s in root if s != '']
        print(root)
        result = []
        
        for i in range(len(root)):
            if root[i] == '.':
                continue
            elif root[i] == '..':
                if len(result) >= 1:
                    result.pop()
            else:
                result.append(root[i])

        if len(result) == 0:
            return '/'
        else:
            s = ''
            for i in result:
                if i != '':
                    s += '/' + i
            return s if s != '' else '/'