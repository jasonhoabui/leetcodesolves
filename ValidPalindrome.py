class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        if len(s) == 0 or len(s) == 1:
            return True
        if s[0] == s[-1]:
            return self.isPalindrome(s[1:-1])
        return False