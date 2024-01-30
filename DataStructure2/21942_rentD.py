import sys
import datetime as dt
from collections import defaultdict

f_i = sys.stdin.readline().strip().split(' ')

n = int(f_i[0])
dhm = f_i[1].split('/')
h,m = dhm[1].split(':')
l=int(dhm[0])*24*60+int(h)*60+int(m)
f = int(f_i[2])

inps = [sys.stdin.readline().strip() for _ in range(n)]
dic={}
fs =defaultdict(int)
for i in inps:
    s_i = i.split(' ')
    date = dt.datetime.strptime(s_i[0]+ s_i[1], '%Y-%m-%d%H:%M')
    item = s_i[2]+' ' + s_i[3]
    if item in dic:
        sub = (int((date - dic[item]).total_seconds()/60) - l)*f
        if sub > 0:
            name = item.split(' ')[1]
            fs[name] += sub
        del dic[item]
    else:
        dic[item] = date
        
if not fs:
    print(-1)
else:
    for name in sorted(fs):
        print(f'{name} {fs[name]}')