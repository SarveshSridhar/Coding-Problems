# Write your code here
testcases = int(input())
for i in range(testcases):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    check = 0
    for j in range(len(a)):
        if abs(a[i])<=k:
            continue
        else:
            check = 1
    count = 0
    if sum(a) == 0 or check == 1:
        count = 0
    else:
        s = sum(a)
        if s>0:
            while(True):
                if s <= 0:
                    break
                s = s - k
                count += 1
        else:
            while(True):
                if s >= 0:
                    break
                s = s + k
                count += 1
    print(count)
