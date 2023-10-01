
str_input = input().strip()
arr = [['' for _ in range(1000)] for _ in range(1000)]
counts = 0
column = 0
row = 0
r = 0
l = 0

for i in range(len(str_input)):
    if str_input[i] == 'L':
        l += 1
        arr[row][column] = 'L'
    else:
        r += 1
        arr[row][column] = 'R'
    column += 1
    if r == l:
        counts += 1
        column = 0
        row += 1
        r = 0
        l = 0

print(counts)
for i in range(1000):
    if arr[i][0] == 'L' or arr[i][0] == 'R':
        print("".join(arr[i]))
        counts -= 1

    if counts == 0:
        break