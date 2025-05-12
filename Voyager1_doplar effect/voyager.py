import numpy as np
import matplotlib.pyplot as plt

freq = 2.9296875e6

time_interval_per_row = 1/freq
print("time_interval in seconds:", time_interval_per_row)

fft_len = 3145728
resolution = freq / fft_len
print("resolution in Hz:", resolution)
total_num_bytes = 4 * 3145728 * 252
time = 252 * time_interval_per_row
print("time in seconds:", time)

total_observation = 3145728 * 252


drift = 6.66

drift_rate = drift / time

print("drift_rate in Hz:", drift_rate)

drift_rate_per_cell = drift_rate/(freq)
print("drift_rate_per_row in hz per cell:", drift_rate_per_cell)

divisible = 1 / drift_rate_per_cell
print("divisible:", divisible)


