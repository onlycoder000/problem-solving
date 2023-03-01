class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefx=[]
        ln=len(strs[0])
        if len(strs) > 1:
            for i in range(0,ln+1):
                d='_'+strs[0][0:i]
                print(d)
                ok=True
                for s in strs:
                    if d not in "_"+s:
                        ok=False
                if ok:
                    prefx.append(d[1:len(d)])
        else:
            return strs[0]
        if prefx:
            # print(prefx)
            return prefx[-1]
        else:
            return ''

            




d=Solution()
print(d.longestCommonPrefix(["flower","flow","flight"]))
# print(d.longestCommonPrefix(["dog","racecar","car"]))
print(d.longestCommonPrefix(["flower","flower","flower","flower"]))
# print(d.longestCommonPrefix([""]))
# print(d.longestCommonPrefix(["a"]))