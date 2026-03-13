n,s = map(int, input().split())
vec = list(map(int, input().split()))


for i in range(n-1):
    for j in range(i+1,n):
        if vec[i] + vec[j] == s:
            print("SI")
            exit(0)
print("NO")