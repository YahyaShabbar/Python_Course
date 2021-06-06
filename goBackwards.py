data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]

minValid = 100
maxValid = 200

# for index in range(len(data) - 1, - 1, - 1):
#     if data[index] < minValid or data[index] > maxValid:
#         print(index, data)
#         del data[index]

topIndex = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < minValid or value > maxValid:
        print(topIndex - index, value)
        del data[topIndex - index]

print(data)