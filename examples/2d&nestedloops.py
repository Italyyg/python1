# 2d list
# list in a list
number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[2][1])
# the row index, the column index. Both start at zero

# using a nested forloop
# col gives us individual items in the row
for row in number_grid:
    for col in row:
        print(col)