
#https://leetcode.com/problems/long-pressed-name

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        j = 0
        for i in range(len(name)):
            if j>=len(typed):
                return False
            if name[i] != typed[j]:
                return False
            if i<len(name)-1:
                while j<len(typed)-1 and name[i] != name[i+1] and typed[j] == typed[j+1]:
                    j+=1
            else:
                while j<len(typed)-1 and typed[j] == typed[j+1]:
                    j+=1
            j+=1
        return j >= len(typed)