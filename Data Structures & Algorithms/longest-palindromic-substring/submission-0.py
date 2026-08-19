class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        def expand(ptr1, ptr2):
            while ptr1 >= 0 and ptr2 < len(s) and s[ptr1] == s[ptr2]:
                ptr1 -= 1
                ptr2 += 1
            return s[ptr1 + 1 : ptr2]

        for i in range(0, len(s)):
            p1 = expand(i, i)
            p2 = expand(i, i + 1)
            
            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2

        return res

        



        