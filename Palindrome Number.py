class Solution:
    def isPalindrome(self, x: int) -> bool:
        n1=str(x)
        n2=n1[::-1]
        if int(n1) - int(n2) == 0:
            return True
        else:
            return False


d=Solution()

print(d.isPalindrome(0))



# print(d.isPalindrome('121'))
# print(d.isPalindrome('125'))
# print(d.isPalindrome('1221'))
# print(d.isPalindrome('1212'))
# print(d.isPalindrome('525'))