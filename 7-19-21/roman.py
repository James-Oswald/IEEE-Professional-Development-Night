
#https://leetcode.com/problems/roman-to-integer/submissions/

class Solution:
    def romanToInt(self, s: str) -> int:
        conv = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        value = 0
        while s != "":
            if len(s) > 1 and conv[s[1]] > conv[s[0]]:
                value += conv[s[1]] - conv[s[0]]
                s = s[2:]
            else:
                value += conv[s[0]]
                s = s[1:]
        return value