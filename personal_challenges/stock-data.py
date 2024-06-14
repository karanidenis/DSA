            # Date    
        # | 5/5 | 5/8 | 5/13 |
# Ms      | 100 | 200 |      | 100      100   -100  
# aws     |     | 50  | 100  | 0
# pal     | 200 |     | 100  | 200
# Total    | 300 | 450 | 400 | 400

# Updated ms:  [100, 200, 200] --> [100, 100, 0]
# Updated aws: [0, 50, 100]    --> [0,   50,   50]
# Updated pal: [200, 200, 100] --> [200,  0,  -100]
#                                  [300,  450,  400]
stock_1 = {
    'ms': 100,
    'aws': 0,
    'pal': 200
}

stock_2 = {
    'ms': 200,
    'aws': 50,
    'pal': 0
}

stock_3 = {
    'ms': 0,
    'aws': 100,
    'pal': 100
}

trades = {name: [] for name in stock_1.keys()}
new_trades = {key: [] for key in stock_1.keys()}


stocks = [stock_1, stock_2, stock_3]
# print(stocks)
    
for stock in stocks:
    for key in stock.keys():
        trades[key].append(stock[key])
# print(trades)

for key, values in trades.items():
    # print(f"{key}: {values}")
    # Replace 0 with the previous value in the list
    for i in range(1, len(values)):
        if values[i] == 0:
            values[i] = values[i - 1]
# print(trades)

for key, values in trades.items():
    new_trades[key].append(values[0])

for key, values in trades.items():
    for i in range(1, len(values)):
        difference = values[i] - values[i - 1]
        new_trades[key].append(difference)
    print(new_trades)

column_sums = [0] * len(list(new_trades.values())[0])
# print(f"{column_sums} columns")

for key, values in new_trades.items():
    for i in range(len(values)):
        column_sums[i] += values[i]

for i in range(1, len(column_sums)):
    column_sums[i] += column_sums[i - 1]

for i, col_sum in enumerate(column_sums):
    print(f"Sum of column {i + 1}: {col_sum}")
