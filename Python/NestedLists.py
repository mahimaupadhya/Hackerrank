if __name__ == '__main__':
    m=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        m.append([name,score])
    li=[marks for name, marks in m]
    b=min(li)
    while min(li)==b:
        li.remove(b)
    names=sorted([d[0] for d in m if min(li)==d[1]])
    for i in names:
        print(i)

