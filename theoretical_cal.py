#!/usr/bin/env python3
"""
Theoretical complexity analysis: T(n) = C * (log n * log log n)

This module calculates theoretical performance times based on experimental data.

Author: Fan
Date: 2025-09-26
"""

import math

def calculate_and_save_theoretical_times(c_value, lines):
    """
    Calculate theoretical times for all n values using computed constant C and save to new file.
    
    Args:
        c_value (float): Computed constant for theoretical time calculation
        lines (list): All lines from experimental_results.txt
    
    Returns:
        None
    """
    # Prepare data for saving theoretical times
    theoretical_results = [
        "Project 1 - Theoretical Time Results",
        "="*40,
        "N\t\tTheoretical Time (seconds)",
        "-"*40
    ]
    
    # Display results header
    print("\n" + "=" * 60)
    print("THEORETICAL RESULTS:")
    print("=" * 60)
    
    # Find and process all data lines
    for line in lines:
        line = line.strip()
        # Find lines containing scientific notation format data
        if 'e+' in line or 'e-' in line:
            try:
                parts = line.split()
                n = float(parts[0])  # N value
                
                # Calculate theoretical time
                log_n = math.log(n)
                log_log_n = math.log(log_n)
                theoretical_time = c_value * (log_n * log_log_n)
                
                # Display and save simultaneously
                print(f"N = {n:>15,.0f} | Time = {theoretical_time:.6e} seconds")
                
                # Format for saving
                n_str = f"{n:.3e}"
                time_str = f"{theoretical_time:.6e}"
                theoretical_results.append(f"{n_str}\t{time_str}")
                
            except (ValueError, IndexError) as e:
                print(f"Error parsing line: {line}, {e}")
                continue
    
    # Add notes
    theoretical_results.extend([
        "-"*40,
        "Note: Theoretical times calculated using formula C * (log n * log log n)",
        f"Where C = {c_value:.6e}",
        ""
    ])
    
    # Save to file
    try:
        with open('theoretical_results.txt', 'w') as file:
            for line in theoretical_results:
                file.write(line + '\n')
        print(f"\nResults have been saved to 'theoretical_results.txt'.")
    except Exception as e:
        print(f"Error saving file: {e}")

def calculate_c_from_results(c_calculation_row=0):
    """
    Read n value and result from specified line in experimental_results.txt file, then calculate constant C.
    
    Args:
        c_calculation_row (int): Index of data row to use for calculating C (default: 0)
    
    Returns:
        float: Calculated constant C, or None if calculation fails
    """
    try:
        # Read experimental_results.txt file
        with open('experimental_results.txt', 'r') as file:
            lines = file.readlines()
        
        # Find all data lines (skip headers and separators)
        data_lines = []
        for line in lines:
            line = line.strip()
            # Find lines containing scientific notation format data
            if 'e+' in line or 'e-' in line:
                data_lines.append(line)
        
        if not data_lines:
            raise ValueError("No valid data lines found")
        
        # Check if index is valid
        if c_calculation_row < 0 or c_calculation_row >= len(data_lines):
            print(f"Using first data row (index 0)")
            c_calculation_row = 0
        
        # Get specified data row
        data_line = data_lines[c_calculation_row]
        
        # Parse data row to extract N value and time
        parts = data_line.split()
        n = float(parts[0])  # N value
        measured_time = float(parts[1])  # Time value
        
        print(f"Using data row {c_calculation_row + 1}/{len(data_lines)}: N = {n:,.0f}, Time = {measured_time:.6e}")
        
        # Calculate constant C
        log_n = math.log(n)
        log_log_n = math.log(log_n)
        
        c_value = measured_time / (log_n * log_log_n)
        print(f"Calculated constant C = {c_value:.6e}")
          
        # Calculate theoretical times for all n values and save
        calculate_and_save_theoretical_times(c_value, lines)
        
        return c_value
        
    except FileNotFoundError:
        print("Error: Cannot find experimental_results.txt file")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Execute function
if __name__ == "__main__":
    c_value = calculate_c_from_results()
    if c_value is not None:
        print(f"\nFinal result: Constant C = {c_value:.6e}")
