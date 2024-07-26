import numpy as np

def ema(values , period) : 

    ema_values = []
    multiplier = 2 / (period + 1)

    for index in range(len(values)) : 

        if index < period - 1 : ema_values.append(None)
        elif index == period - 1 : ema_values.append(np.mean(values[: period]))
        else : ema_values.append((values[index] - ema_values[-1]) * multiplier + ema_values[-1])
    
    return ema_values

def calculate_gmma(close_prices) : 

    short_periods = [3, 5, 8, 10, 12, 15]
    long_periods = [30, 35, 40, 45, 50, 60]

    short_emas = []
    long_emas = []

    for period in short_periods : short_emas.append(ema(close_prices, period))
    for period in long_periods : long_emas.append(ema(close_prices, period))

    return short_emas , long_emas

# Example usage:
close_prices = [115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 305]
short_emas, long_emas = calculate_gmma(close_prices)

# Print results
print("Short-term EMAs:")
for index, period in enumerate([3, 5, 8, 10, 12, 15]):
    print(f"EMA {period}: {short_emas[index]}")

print("\nLong-term EMAs:")
for index, period in enumerate([30, 35, 40, 45, 50, 60]):
    print(f"EMA {period}: {long_emas[index]}")
