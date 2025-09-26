#!/usr/bin/env python3
"""
Project 1 - Algorithm Performance Analysis

Main module for algorithm performance analysis and comparison.

Author: Fan
Date: 2025-09-26
"""

import time
from theoretical_cal import calculate_c_from_results
from graph import plot_comparison

def option_0(n):
    """
    Algorithm implementation - Option 0.
    
    Implements a nested loop algorithm with specific complexity characteristics.
    
    Args:
        n (int): Input size for the algorithm
    
    Returns:
        int: Sum calculated by the algorithm
    """
    sum_value = 0
    j = 2  
    while j < n:
        k = j
        while k < n:
            sum_value += 1
            k = k * k
        j = 2 * j
    return sum_value

def time_measure(n, trials=5):
    """
    Measure the execution time of option_0 algorithm.
    
    Args:
        n (int): Input size for the algorithm
        trials (int): Number of trials to run (default: 5)
    
    Returns:
        float: Average execution time after removing outliers
    """
    times = []
    for _ in range(trials):
        t0 = time.perf_counter()
        option_0(n)
        t1 = time.perf_counter()
        times.append(t1 - t0)

    times.sort()
    # Remove outliers (fastest and slowest measurements)
    times = times[1:-1]  

    return sum(times) / len(times)

def run_performance_analysis():
    """
    Run performance analysis and save results to file.
    
    Executes the algorithm with various input sizes, measures execution times,
    and saves results to 'experimental_results.txt'.
    
    Returns:
        None
    """   
    # Define n values
    n_values = [10**k for k in range(1, 14, 2)]  # 10¹, 10³, 10⁵, ..., 10¹³
    
    print(f"\ninput sizes: {len(n_values)} , N values: {[f'{n:,.0f}' for n in n_values]}")
    
    # Measure performance
    data = []
    for i, n in enumerate(n_values, 1):
        print(f"\nTest {i}/{len(n_values)}: N = {n:,}")
        t = time_measure(n)
        data.append((n, t))
        print(f"Time: {t:.6e} seconds")
    
    # Display results
    print("\n" + "=" * 60,"\nPERFORMANCE RESULTS:","\n","=" * 60)
    for n, t in data:
        print(f"N = {n:>15,} | Time = {t:.6e} seconds")
    
    # Save results to file
    save_results_to_file(data)

def save_results_to_file(data):
    """
    Save performance results to experimental_results.txt file.
    
    Args:
        data (list): List of (n, time) tuples containing performance measurements
    
    Returns:
        None
    """
    with open('experimental_results.txt', 'w') as f:
        f.write("Project 1 - Algorithm Performance Results\n")
        f.write("========================================\n")
        f.write("N\t\tTime (seconds)\n")
        f.write("----------------------------------------\n")
        for n, t in data:
            f.write(f"{n:.3e}\t{t:.6e}\n")
        f.write("----------------------------------------\n")
        f.write("Note: Time measurements are in seconds using scientific notation.\n")
    
    print(f"\nResults have been saved to 'experimental_results.txt'.")

def run_theoretical_analysis(c_calculation_row=0):
    """
    Run theoretical analysis to calculate constant C and generate theoretical times.
    
    Args:
        c_calculation_row (int): Index of data row to use for calculating C (default: 0)
    
    Returns:
        None
    """
    try:
        c_value = calculate_c_from_results(c_calculation_row)
        if c_value is not None:
            print("Theoretical analysis completed successfully!")
        else:
            print("Error: Failed to calculate constant C")
    except Exception as e:
        print(f"Error running theoretical analysis: {e}")

def generate_comparison_graph():
    """
    Generate comparison graph between experimental and theoretical results.
    
    Creates and displays a visual comparison of experimental vs theoretical performance data.
    
    Returns:
        None
    """
    try:
        plot_comparison()
    except Exception as e:
        print(f"Error generating graph: {e}")

def main():
    """
    Main function - Complete analysis pipeline.
    
    Executes three-step analysis:
    1. Measure algorithm performance experimentally
    2. Calculate theoretical times using constant C
    3. Generate comparison graph
    
    Returns:
        None
    """
    print("Starting complete algorithm analysis pipeline...\n")
    
    # Run experimental performance analysis
    run_performance_analysis()
    
    # Calculate theoretical predictions
    run_theoretical_analysis(3)
    
    # Generate comparison graph
    generate_comparison_graph()


if __name__ == "__main__":
    main()
