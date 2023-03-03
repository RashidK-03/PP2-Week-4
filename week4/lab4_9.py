N = int(input())
def gensquares(N):
    for i in range(N):
        yield i**2
for x in gensquares(N):
    print(x)