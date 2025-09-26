# Project 1

## Overview
This project analyzes the performance of a nested loop algorithm through experimental measurements and theoretical calculations. The algorithm has time complexity `O(log n * log log n)`.

## Files
- `main.py` - Main program with algorithm implementation and timing
- `Graph.py` - Creates comparison charts between experimental and theoretical results
- `Theoretical_Cal.py` - Calculates theoretical time predictions
- `mini_test.py` - Unit tests for core functionality
- `experimental_results.txt` - Measured execution times
- `theoretical_results.txt` - Theoretical time predictions

## Algorithm
```python
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
```

## How to Run

### Complete Analysis
```bash
python main.py
```
This runs the full pipeline: experimental measurement → theoretical calculation → visualization

### Run Tests
```bash
python mini_test.py
```

## Requirements
- Python 3.7+
- matplotlib
- numpy

Install dependencies:
```bash
pip install matplotlib numpy
```

## Output
- `experimental_results.txt` - Timing measurements for different input sizes
- `theoretical_results.txt` - Calculated theoretical times using constant C
- `algorithm_performance_comparison.png` - Log-log comparison chart

## Results
The program tests input sizes from 10¹ to 10¹³ and compares experimental vs theoretical performance, typically achieving accuracy within 5-15%.