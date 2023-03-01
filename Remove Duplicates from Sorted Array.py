class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        x=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[x]=nums[i]
                x+=1
        return x


d=Solution()
print(d.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))