sentinel = 1
numbers = []
while sentinel != -1:

    number_str = input("Enter a number or press -1 to quit")
    number = int(number_str)
    if number == -1:
        sentinel = -1
        break
    numbers.append(number)
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print(f"smallest values is {smallest}")
