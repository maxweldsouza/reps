def buy_sell(arr):
    minimum = arr[0]
    max_profit = 0
    for item in arr:
        if item < minimum:
            minimum = item
        elif item - minimum > max_profit:
            max_profit = item - minimum
    return max_profit

print buy_sell([310, 315, 275, 260, 270, 290, 230, 255, 250])
