if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg=0
    l=list()
    l=student_marks[query_name]
    for i in l:
        avg+=i
    print('%.2f' %(avg/len(l)))
