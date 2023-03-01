class Solution:
    def romanToInt(self, s: str) -> int:
        I=str(1)+','
        V=str(5)+','
        X=str(10)+','
        L=str(50)+','
        C=str(100)+','
        D=str(500)+','
        M=str(1000)+','
        data=s.lower().replace('i',I)
        data=data.lower().replace('v',V)
        data=data.lower().replace('x',X)
        data=data.lower().replace('l',L)
        data=data.lower().replace('c',C)
        data=data.lower().replace('d',D)
        data=data.lower().replace('m',M)
        data=data.split(',')
        data=[x for x in data if x!='']
        
        r=0
        c=0
        for i in data:
            if(i):
                i=int(i)
                if c==0:
                    prev=0
                else:
                    prev=int(data[c-1])
                try:
                    next=int(data[c+1])
                except:
                    next=False
                
                if(next > i):
                    r+=(i-(i*2))
                else:
                    r+=i

                print(prev,i,next,r)
            else:
                i=0
            c+=1
        return r


#M-C-M-X-C-I-V=1000+(-100)+1000+(-10)+100+(-1)+5=1194
#L-V-I-I-I=50+5+1+1+1=58
#I-V=(-1)+5=4



cl=Solution()
print(cl.romanToInt('IV'))








