import numpy as np

def moving_average(sequence, k):
    n = len(sequence)
    moving_avg = []
    for i in range(n - k + 1):
        window = sequence[i:i+k]
        avg = np.mean(window)
        moving_avg.append(avg)
    return moving_avg

# Test the function
sequence = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
k = 7
print("Moving average sequence with k =", k, ":", moving_average(sequence, k))
