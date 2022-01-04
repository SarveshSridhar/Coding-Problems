# Write your code here
testcases = int(input())

for t in range(testcases):
    n,k = map(int, input().split())
    a = input()
    max = ''
    p = -1
    for i in range(n):
        if max<a:
            max = a
            d = i
        elif max == a:
            p = i-d
            break
        a = a[1:]+a[:1]
    if p == -1:
        printing = d+(k-1)*n
        print(printing)
    else:
        printing = d+(k-1)*p
        print(printing)
        
