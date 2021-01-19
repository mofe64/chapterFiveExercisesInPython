import math


class Interest:
    def __init__(self, principal, rate):
        self.principal = principal
        self.rate = rate

    def calculate_interest(self, year):
        amount = self.principal * ((1.0 + self.rate) ** year)
        return amount

    def change_rate(self, rate):
        self.rate = rate
