n=int(input())
s=set(map(int,input().split()))
t=int(input())
for i in range(t):
    b,c=map(str,input().split())
    diffset=set(map(int,input().split()))
    getattr(s,b)(diffset)
print(sum(s))
