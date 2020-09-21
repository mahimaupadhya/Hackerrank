def average(array):
    b=set(array)
    return (sum(b)/len(b))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
