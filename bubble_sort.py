numbers = [4, 10, 5, 8, 1, 2, 3, 9, 6, 7]

for i in range(9):
    for j in range(9):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)