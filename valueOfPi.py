max_term = 20
start_term = 0
no_of_iterations_so_far = 0
constant = 4
variable_numerator = 4
variable_denominator = 3
while start_term < max_term:
    pi = constant - (variable_numerator / variable_denominator)
    # print(variable_denominator)
    variable_denominator += 2
    start_term += 1
    no_of_iterations_so_far += 1
    if pi == 3.14159:
        print(f"3.14159 found in {no_of_iterations_so_far} iterations")
        break
    print(f"pi value is {pi}")