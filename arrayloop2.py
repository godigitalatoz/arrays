# Create a 4x4 array
array_4x4 = [[0 for _ in range(4)] for _ in range(4)]

# Write values to the array using nested loops
for i in range(4):
    for j in range(4):
        array_4x4[i][j] = i * 4 + j + 1

# Print the array
for row in array_4x4:
    print(row)
