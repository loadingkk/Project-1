#!/usr/bin/env python3
"""
Compare theoretical and experimental algorithm performance

This module generates comparison graphs and analyzes performance data.

Author: Zhentao Fan
Date: 2025-09-26
"""

import matplotlib.pyplot as plt
import numpy as np

def read_results_data(filename):
    """
    Read data from results file.
    
    Args:
        filename (str): File name to read data from
    
    Returns:
        tuple: A tuple containing (n_values, time_values) where:
            - n_values (list): List of N values
            - time_values (list): List of time values
    """
    n_values = []
    time_values = []
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Find and parse data lines
        for line in lines:
            line = line.strip()
            # Find lines containing scientific notation format data
            if 'e+' in line or 'e-' in line:
                try:
                    parts = line.split()
                    n = float(parts[0])  # N value
                    time = float(parts[1])  # Time value
                    n_values.append(n)
                    time_values.append(time)
                except (ValueError, IndexError):
                    continue
    
    except FileNotFoundError:
        print(f"Error: Cannot find file {filename}")
    
    return n_values, time_values

def plot_comparison():
    """
    Plot comparison chart of experimental and theoretical times.
    
    Creates a log-log scale plot comparing experimental vs theoretical performance data.
    Saves the plot as 'algorithm_performance_comparison.png' and displays comparison statistics.
    
    Returns:
        None
    """
    # Read experimental data
    exp_n, exp_time = read_results_data('experimental_results.txt')
    
    # Read theoretical data
    theo_n, theo_time = read_results_data('theoretical_results.txt')
    
    if not exp_n or not theo_n:
        print("Error: Unable to read data files")
        return
    
    # Create figure
    plt.figure(figsize=(12, 8))
    
    # Plot data points
    plt.loglog(exp_n, exp_time, 'ro-', label='Experimental Time', markersize=8, linewidth=2)
    plt.loglog(theo_n, theo_time, 'bs-', label='Theoretical Time', markersize=8, linewidth=2)
    
    # Set figure properties
    plt.xlabel('N (Input Size) - Log Scale', fontsize=12)
    plt.ylabel('Time (seconds) - Log Scale', fontsize=12)
    plt.title('Algorithm Performance Comparison: Experimental vs Theoretical Time\n(Log-Log Scale)', fontsize=14)
    
    
    # Improve grid for log scale
    plt.grid(True, which='major', alpha=0.5, linestyle='-')
    plt.grid(True, which='minor', alpha=0.2, linestyle='--')
    plt.legend(fontsize=11)
    
    # Add data annotations
    for i, (n, t) in enumerate(zip(exp_n, exp_time)):
        plt.annotate(f'N={n:.0e}\nT={t:.2e}', 
                    (n, t), 
                    xytext=(10, 10), 
                    textcoords='offset points',
                    fontsize=9,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='red', alpha=0.3))
    
    for i, (n, t) in enumerate(zip(theo_n, theo_time)):
        plt.annotate(f'N={n:.0e}\nT={t:.2e}', 
                    (n, t), 
                    xytext=(-40, -20), 
                    textcoords='offset points',
                    fontsize=9,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='blue', alpha=0.3))
    
    # Display and save figure
    plt.tight_layout()
    plt.savefig('algorithm_performance_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Print data comparison
    print("\nData Comparison:")
    print("="*60)
    print(f"{'N':>12} {'Experimental':>15} {'Theoretical':>15} {'Relative Error':>15}")
    print("-"*60)
    
    for i in range(len(exp_n)):
        if i < len(theo_n):
            relative_error = abs(exp_time[i] - theo_time[i]) / exp_time[i] * 100
            print(f"{exp_n[i]:>12.0e} {exp_time[i]:>15.6e} {theo_time[i]:>15.6e} {relative_error:>11.1f}%")

if __name__ == "__main__":
    plot_comparison()
