class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            scount = {}
            for char in s:
                scount[char] = scount.get(char, 0) + 1
            for char in t:
                if char in scount:
                    scount[char] -= 1
                else:
                    return False

            for char in scount:
                if scount[char] != 0:
                    return False
            else:
                return True