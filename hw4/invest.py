def invest(amount: float, rate: float, years: int):
    i = 1
    while i <= years:
        amount = amount * (1 + rate)
        print('year ', i, ': $', round(amount, 2))
        i = i + 1
amount = float(input('Input the amount: '))
rate = float(input('Input the rate of interest: '))
years = int(input('Input the number of years: '))
invest(amount, rate, years)