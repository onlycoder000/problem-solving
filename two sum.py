class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        r=[]
        find=False
        c=0
        for i in nums:
            n1=i
            n2=target - n1

            c2=0
            for i2 in nums:
                print(c,c2)
                if c==c2:
                    c2+=1
                    continue
                else:
                    if(i2==n2):
                        print(c2)
                        find=True
                        break
                c2+=1

            if find:
                break

            c+=1

        r.append(c)
        r.append(c2)
        return r
d=Solution()
print(d.twoSum([3,3], 6))