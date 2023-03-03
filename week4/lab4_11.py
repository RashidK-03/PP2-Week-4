n = int(input())
divisGenerator = (i for i in range(n))
for i in divisGenerator:
    if (i % 3 == 0) and (i % 4 == 0):
        print(i)