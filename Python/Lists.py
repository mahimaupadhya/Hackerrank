if __name__ == '__main__':
    N = int(input())
    li=list()
    for i in range(N):
        inp=list(map(str,input().split()))
        if inp[0]=="insert":
            li.insert(int(inp[1]),int(inp[2]))
        elif inp[0]=="pop":
            li.pop()
        elif inp[0]=="append":
            li.append(int(inp[1]))
        elif inp[0]=="reverse":
            li.reverse()
        elif inp[0]=="sort":
            li.sort()
        elif inp[0]=="remove":
            li.remove(int(inp[1]))
        else:
            print(li)
        
