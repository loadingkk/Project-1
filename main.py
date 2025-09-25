#Project 1

import time

def Option_0(n):
    Sum = 0
    j = 2
    while j < n:
        k = j
        while k < n:
            Sum += 1
            k = k * k
        j = 2 * j
    return Sum

def Time_Measure(n, trials=5):

    best = float('inf')
    for _ in range(trials):
        t0 = time.perf_counter()
        Option_0(n)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return best

Ns = [10**k for k in (3,6,9)]  # From 1,000 to 100,000,000
data = [(n, Time_Measure(n)) for n in Ns]
for n,t in data:
    print(n, t)

# 将结果记录到txt文件中，使用科学计数法
with open('results.txt', 'w') as f:
    f.write("Project 1 - Algorithm Performance Results\n")
    f.write("========================================\n")
    f.write("N\t\tTime (seconds)\n")
    f.write("----------------------------------------\n")
    for n, t in data:
        f.write(f"{n:.3e}\t{t:.6e}\n")
    f.write("----------------------------------------\n")
    f.write("Note: Time measurements are in seconds using scientific notation.\n")

print("\nResults have been saved to 'results.txt' in scientific notation format.")
