product_price_list = {
    1: 2.98,
    2: 4.50,
    3: 9.98,
    4: 4.49,
    5: 6.87
}
sentinel = 1
total_retail_value = 0
while sentinel != -1:
    product_number_str = input("Enter Product number or -1 to quit ")
    product_number = int(product_number_str)
    if product_number == -1:
        sentinel = -1
        break
    product_quantity_str = input("Enter quantity sold or -1 to quit ")
    product_quantity = int(product_number_str)
    if product_quantity == -1:
        sentinel = -1
        break
    item_price = product_price_list.get(product_number, -1)
    if item_price == -1:
        print("Invalid product number")
        continue
    retail_value = item_price * product_quantity
    total_retail_value += retail_value
    print(f"retail value is {retail_value}")
    print(f"total retail value so far is {total_retail_value}")
