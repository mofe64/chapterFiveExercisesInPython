from compundInterestCalculator import Interest

interest = Interest(1000, 0.05)
rate = 5
max_rate = 10
while rate <= max_rate:
    print(interest.calculate_interest(10))
    interest.change_rate(rate/100)
    rate += 1
