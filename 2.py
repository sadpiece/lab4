n = 7

a = [[max(i - j + 1, 0) for i in range(n)] for j in range(n)]

for r in a:
    print(*r)