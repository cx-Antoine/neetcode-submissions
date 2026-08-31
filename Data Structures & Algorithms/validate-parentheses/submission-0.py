class Solution:
    def isValid(self, s: str) -> bool:

        match = {
            "{" : "}",
            "[" :  "]",
            "(" :  ")"
        }

        pairs = []


        for i in range(len(s)):
            if s[i] in match:
                pairs.append(s[i])
            else:
                if len(pairs) == 0:
                    return False
                else:
                    most_recent = pairs.pop()
                    if match[most_recent] != s[i]:
                        return False
        
        if len(pairs) == 0:
            return True
        else:
            return False
            



                
            

        