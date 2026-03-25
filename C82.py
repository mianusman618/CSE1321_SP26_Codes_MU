numbers=[50,4,36,100,23,2,90,1]
print(numbers)
#numbers = [3, 5, 2, 7]
length = len(numbers)
for i in range(length):
    for index in range(length - i - 1):
        if numbers[index] < numbers[index + 1]:
            temp = numbers[index]
            numbers[index] = numbers[index + 1]
            numbers[index + 1] = temp
print(numbers)

