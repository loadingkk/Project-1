# Project 1 

import time
from Theoretical_Cal import calculate_C_from_results
from Graph import plot_comparison

def Option_0(n):
    """
    Algorithm implementation - Option 0

    """
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
    """
    Measure the execution time of Option_0 algorithm
    
    Parameters:
    n: Input size
    trials: Number of trials to run (default: 5)
    
    Returns:
    avg_time: Average time after removing outliers
    """
    times = []
    for _ in range(trials):
        t0 = time.perf_counter()
        Option_0(n)
        t1 = time.perf_counter()
        times.append(t1 - t0)

    times.sort()
    # Remove outliers (fastest and slowest measurements)
    times = times[1:-1]  

    return sum(times) / len(times)

def run_performance_analysis():
    """
    Run performance analysis and save results to file
    """   
    # Define n values
    Ns = [10**k for k in range(1, 14, 2)]  # 10¹, 10³, 10⁵, ..., 10¹³
    
    print(f"\ninput sizes: {len(Ns)} , N values: {[f'{n:,.0f}' for n in Ns]}")
    
    # Measure performance
    data = []
    for i, n in enumerate(Ns, 1):
        print(f"\nTest {i}/{len(Ns)}: N = {n:,}")
        t = Time_Measure(n)
        data.append((n, t))
        print(f"Time: {t:.6e} seconds")
    
    # Display results
    print("\n" + "=" * 60,"\nPERFORMANCE RESULTS:","\n","=" * 60)
    for n, t in data:
        print(f"N = {n:>15,} | Time = {t:.6e} seconds")
    
    # Save results to file
    save_results_to_file(data)
    
    return data

def save_results_to_file(data):
    """
    Save performance results to experimental_results.txt file
    
    Parameters:
    data: List of (n, time) tuples
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

def run_theoretical_analysis(data_row_index=0):
    """
    Run theoretical analysis to calculate constant C and generate theoretical times
    
    Parameters:
    data_row_index: Index of data row to use for calculating C (default: 0 for first row)
    """
    try:
        C = calculate_C_from_results(data_row_index)
        if C is not None:
            print("Theoretical analysis completed successfully!")
        else:
            print("Error: Failed to calculate constant C")
    except Exception as e:
        print(f"Error running theoretical analysis: {e}")

def generate_comparison_graph():
    """
    Generate comparison graph between experimental and theoretical results
    """
    try:
        plot_comparison()
    except Exception as e:
        print(f"Error generating graph: {e}")

def main():
    """
    Main function - Complete analysis pipeline
    Executes three-step analysis:
    1. Measure algorithm performance experimentally
    2. Calculate theoretical times using constant C
    3. Generate comparison graph
    """
    print("Starting complete algorithm analysis pipeline...\n")
    
    # Run experimental performance analysis
    data = run_performance_analysis()
    
    # Calculate theoretical predictions
    run_theoretical_analysis(3)
    
    # Generate comparison graph
    generate_comparison_graph()


if __name__ == "__main__":
    main()
