class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 0:
            while True:
                print(s)
                prev=s
                s=s.replace('()','').replace('{}','').replace('[]','')
                if not s:
                    return True
                if prev == s:
                    return False
                
        else:
            return False


d=Solution()
print(d.isValid('{]()'))

print(d.isValid('(()'))
print(d.isValid('{()}'))
print(d.isValid('([{)])'))