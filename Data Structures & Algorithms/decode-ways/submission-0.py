import string

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
            
        # Create valid string mappings ("1" -> 'A', ..., "26" -> 'Z')
        valid_codes = {str(idx): char for idx, char in enumerate(string.ascii_uppercase, start=1)}
        
        # dp[i] will store the number of valid ways to decode s[:i]
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # Base case: empty string has 1 valid decoding way
        dp[1] = 1  # Base case: first character (already checked it's not '0')
        
        for i in range(2, len(s) + 1):
            # 1-digit check: current character
            one_digit = s[i-1:i]
            if one_digit in valid_codes:
                dp[i] += dp[i-1]
                
            # 2-digit check: current character and previous character
            two_digits = s[i-2:i]
            if two_digits in valid_codes:
                dp[i] += dp[i-2]
                
        return dp[-1]