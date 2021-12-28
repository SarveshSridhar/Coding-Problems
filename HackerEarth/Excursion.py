# Write your code here
testcases = int(input())

def check(n, k):
    count = 0
    if n == 0:
        return 0
    if n//k == n/k and n!=0 and k!=0:
        count = n//k
    else:
        count = n//k + 1
    return count

for i in range(testcases):
    n,m,k = map(int, input().split())
    print(check(n,k)+check(m,k))
