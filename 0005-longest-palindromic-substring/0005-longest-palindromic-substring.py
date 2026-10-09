class Solution(object):
    def longestPalindrome(self, s):
        
        if not s:
            return ""
    
        start = 0
        end = 0
    
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # Length of the palindrome

        for i in range(len(s)):
        # Odd-length palindromes (e.g., "aba")
            len1 = expand_from_center(i, i)
        # Even-length palindromes (e.g., "abba")
            len2 = expand_from_center(i, i + 1)
        
            max_len = max(len1, len2)
        
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
            
        return s[start:end + 1]