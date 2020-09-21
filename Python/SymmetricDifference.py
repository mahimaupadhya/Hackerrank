i,set1=input(),set(map(int,input().split()))
j,set2=input(),set(map(int,input().split()))
for i in sorted(set1.symmetric_difference(set2)): print(i)
