import sys
def input():
    return sys.stdin.readline().strip()
ls=[]
c_n = int(input())
for _ in range(c_n):
    n_l = int(input())
    l=list(map(int, input().split(' ')))
    while n_l // 10:
        l+=list(map(int, input().split(' ')))
        n_l -= 10
    ls.append(l)

rs=[]
for l in ls:
    arr=[]
    r=[]
    for idx,el in enumerate(l):
        if not arr or el > arr[-1]:
            arr.append(el)
        else:
            i=0
            while(el>arr[i]):
                i+=1
            arr = arr[:i] + [el] + arr[i:]
        if not idx%2:
            r.append(arr[idx//2])
    rs.append(r)

for r in rs:
    leng =len(r)
    print(leng)
    cnt=0
    for num in r:
        cnt+=1
        if leng==cnt or cnt==10:
            print(num)
        else:    
            print(num,end=' ')