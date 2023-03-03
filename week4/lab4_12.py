a,b = int(input()), int(input())
squaresGenerator = (i * i for i in range(a, b))
for i in squaresGenerator:
    print(i)