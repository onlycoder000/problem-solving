class Solution:
    def mergeTwoLists(self, list1 ,list2):
        r=[]
        for i in range(-101,101):
            if len(list1):
                for z in list1:
                    if i==z:
                        r.append(i)
            if len(list2):
                for z in list2:
                    if i==z:
                        r.append(i)
        return(r)


        
        





d=Solution()
print(d.mergeTwoLists([1,2,4],[1,3,4]))