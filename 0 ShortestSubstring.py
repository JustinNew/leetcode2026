# 76. Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.

# Key is to use a sliding window to find the minimum window substring.
# We can use a hash map to store the frequency of each character in t.
# We can then use a sliding window to find the minimum window substring.
# We can use a hash map to store the frequency of each character in the current window.
# We can then use a hash map to store the frequency of each character in t.
# We can then use a hash map to store the frequency of each character in the current window.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def removeMin(l):
            minN = min(l)
            temp = []
            flag = False
            for i in l:
                if i != minN:
                    temp.append(i)
                elif i == minN and flag == True:
                    temp.append(i)
                else:
                    flag = True
            
            return temp

        def getMin(DicPos):
            minPos = None
            for k in DicPos:
                tMin = min(DicPos[k])
                if minPos == None:
                    minPos = tMin
                else:
                    minPos = min(tMin, minPos)

            return minPos
        
        def getMax(DicPos):
            maxPos = None
            for k in DicPos:
                tMax = max(DicPos[k])
                if maxPos == None:
                    maxPos = tMax
                else:
                    maxPos = max(tMax, maxPos)

            return maxPos

        def dicEqual(d1, d2):
            for k in d1:
                if k not in d2 or d2[k] != d1[k]:
                    return False

            for k in d2:
                if k not in d1 or d1[k] != d2[k]:
                    return False

            return True

        if len(t) > len(s):
            return ""

        tDic = {}
        sDic = {}
        sPos = {}

        for i in t:
            if i in tDic:
                tDic[i] += 1
            else:
                tDic[i] = 1

        begin = 0
        current = 0
        result = ""
        while current < len(s):
            if s[current] in tDic and s[current] not in sDic:
                sDic[s[current]] = 1
                sPos[s[current]] = [current]
            elif s[current] in tDic and sDic[s[current]] < tDic[s[current]]:
                sDic[s[current]] += 1
                sPos[s[current]].append(current)
            elif s[current] in tDic and sDic[s[current]] == tDic[s[current]]:
                if dicEqual(tDic, sDic):
                    begin = getMin(sPos)
                    end = getMax(sPos)
                    if result == "":
                        result = s[begin:end + 1]
                    else:
                        if len(s[begin:end + 1]) < len(result):
                            result = s[begin:end + 1]
                sPos[s[current]] = removeMin(sPos[s[current]])
                sPos[s[current]].append(current)
            
            current += 1

        if dicEqual(tDic, sDic):
            begin = getMin(sPos)
            end = getMax(sPos)
            if result == "":
                result = s[begin:end + 1]
            else:
                if len(s[begin:end + 1]) < len(result):
                    result = s[begin:end + 1]

        return result
        