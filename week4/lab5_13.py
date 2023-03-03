n = int(input())
listGenerator = (i for i in range(n, 0, -1))
for i in listGenerator:
    print(i)