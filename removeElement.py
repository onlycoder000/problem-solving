class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        x=0
        c=0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[c]=nums[i]
                c+=1
            else:
                x+=1
        return c

d=Solution()
print(d.removeElement([3,2,2,3],3))
print(d.removeElement([0,1,2,2,3,0,4,2],2))