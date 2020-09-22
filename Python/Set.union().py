eng=int(input())
eng_list=set(map(int,input().split()))
french=int(input())
french_list=set(map(int,input().split()))
print(len(eng_list.union(french_list)))

