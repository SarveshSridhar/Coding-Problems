n = int(input())
a = list(map(int, input().split()))

def solution(array):
    a1 = array[::-1]
    b1 = array[:]
    output = []
    while True:
        if len(a1) == 0 or len(b1) == 0:
            break
        a = a1[-1]
        b = b1[-1]
        if a>b:
            output.append(1)
            b1.pop()
        elif a<b:
            output.append(2)
            a1.pop()
        else:
            output.append(0)
            a1.pop()
            b1.pop()
    print(*output)
solution(a)
