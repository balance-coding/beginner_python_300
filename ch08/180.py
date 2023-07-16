low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
votality = []

for i in range(5):
    sub = high_prices[i]-low_prices[i]
    votality.append(i)

print(votality)
