col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(col):
    for j in range(row):
        if matrix[i][j] == '*':
            continue
        matrix[i][j] = 0
        for y in range(i - 1, i + 2):
            for x in range(j - 1, j + 2):     
                if y < 0 or x < 0 or y >= row or x >= col:
                    continue
                if matrix[y][x] == '*':
                    matrix[i][j] += 1

for i in matrix:
    for j in i:
        print(j, end='')
    print()
    
    
                    
                    
