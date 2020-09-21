n = int(input())
s = set(map(int, input().split()))
t= int(input())
for i in range(t):
    b,*c=map(str,input().split())
    getattr(s,b)(*(int(x) for x in c))
print(sum(s))
