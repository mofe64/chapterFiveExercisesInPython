counter = 1
product = 1
while counter <= 15:
    if counter % 2 == 1:
        product *= counter
    counter += 1
print(f"product is {product}")
