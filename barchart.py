counter = 0
numbers = []
while counter < 5:
    number_str = input("Enter a number ")
    number = int(number_str)
    numbers.append(number)
    counter += 1

for number in numbers:
    i = 0
    while i < number:
        print("*", end="")
        i += 1
    print("\n")
