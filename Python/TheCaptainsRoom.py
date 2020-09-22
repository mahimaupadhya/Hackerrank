size=int(input())
s=list(map(int,input().split()))
import collections
b=collections.Counter(s)
for x,l in b.items():
    if l==1: print(x)
