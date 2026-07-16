class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        for i in s:
            if i.isalnum():
                continue
            else:
                s=s.replace(i,"")
        a=s[::-1]

        if a==s:
            return True
        else:
            return False