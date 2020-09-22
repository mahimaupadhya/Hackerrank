c=int(input())
for i in range(c):
    noksm=int(input())
    set1=set(map(int,input().split()))
    nokam=int(input())
    set2=set(map(int,input().split()))
    print(set1.issubset(set2))
