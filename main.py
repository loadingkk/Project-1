#Project 1

import time

def kernel(n):
    Sum = 0
    j = 2
    while j < n:
        k = j
        while k < n:
            # 模拟常数工作；访问数组替换为简单加法即可
            Sum += 1
            k = k * k
        j = 2 * j
    return Sum

def measure(n, trials=5):
    # 取最小/中位数可减小波动；这里用最小值
    best = float('inf')
    for _ in range(trials):
        t0 = time.perf_counter()
        kernel(n)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return best

Ns = [10**k for k in range(3, 9)]  # 1e3 ... 1e8，可按机器性能调整
data = [(n, measure(n)) for n in Ns]
for n,t in data:
    print(n, t)
