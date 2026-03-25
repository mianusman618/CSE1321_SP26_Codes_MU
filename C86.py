#numbers = [3, 5, 2, 7]
numbers=[50,500,23,45,78,32,1,32,75,100,90]
print(numbers)
length = len(numbers)
for i in range(length):
    for index in range(length - i - 1):
        if numbers[index] > numbers[index + 1]:
            temp = numbers[index]
            numbers[index] = numbers[index + 1]
            numbers[index + 1] = temp

print(numbers)
