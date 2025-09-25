#Project 1 - Complete Analysis Pipeline

import time
from Theoretical_Cal import calculate_C_from_results
from Graph import plot_comparison

def Option_0(n):
    """
    Algorithm implementation - nested loops with exponential growth
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
    best: Best (minimum) time among all trials
    """
    best = float('inf')
    for _ in range(trials):
        t0 = time.perf_counter()
        Option_0(n)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return best

def run_performance_analysis():
    """
    Run performance analysis and save results to file
    """
    print("=" * 60)
    print("PROJECT 1 - ALGORITHM PERFORMANCE ANALYSIS")
    print("=" * 60)
    
    # Define test cases
    Ns = [10**k for k in range(1, 14, 2)]  # From 10^1 to 10^13, step=2
    
    print(f"\nRunning performance tests for {len(Ns)} different input sizes...")
    print("Input sizes:", [f"10^{k}" for k in range(1, 14, 2)])
    
    # Measure performance
    data = []
    for i, n in enumerate(Ns, 1):
        print(f"\nTest {i}/{len(Ns)}: N = {n:,}")
        t = Time_Measure(n)
        data.append((n, t))
        print(f"Time: {t:.6e} seconds")
    
    # Display results
    print("\n" + "=" * 60)
    print("PERFORMANCE RESULTS:")
    print("=" * 60)
    for n, t in data:
        print(f"N = {n:>15,} | Time = {t:.6e} seconds")
    
    # Save results to file
    save_results_to_file(data)
    
    return data

def save_results_to_file(data):
    """
    Save performance results to results.txt file
    
    Parameters:
    data: List of (n, time) tuples
    """
    with open('results.txt', 'w') as f:
        f.write("Project 1 - Algorithm Performance Results\n")
        f.write("========================================\n")
        f.write("N\t\tTime (seconds)\n")
        f.write("----------------------------------------\n")
        for n, t in data:
            f.write(f"{n:.3e}\t{t:.6e}\n")
        f.write("----------------------------------------\n")
        f.write("Note: Time measurements are in seconds using scientific notation.\n")
    
    print(f"\nResults have been saved to 'results.txt' in scientific notation format.")

def run_theoretical_analysis(data_row_index=0):
    """
    Run theoretical analysis to calculate constant C and generate theoretical times
    
    Parameters:
    data_row_index: Index of data row to use for calculating C (default: 0 for first row)
    """
    print("\n" + "=" * 60)
    print("RUNNING THEORETICAL ANALYSIS...")
    print("=" * 60)
    
    try:
        # Direct function call with specified data row index
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
    print("\n" + "=" * 60)
    print("GENERATING COMPARISON GRAPH...")
    print("=" * 60)
    
    try:
        # Direct function call instead of subprocess
        plot_comparison()
        print("Graph generation completed successfully!")
        print("Graph saved as 'algorithm_performance_comparison.png'")
    except Exception as e:
        print(f"Error generating graph: {e}")

def main():
    """
    Main function - Complete analysis pipeline
    """
    print("Starting complete algorithm analysis pipeline...\n")
    
    # Step 1: Run performance analysis
    data = run_performance_analysis()
    
    # Step 2: Run theoretical analysis
    run_theoretical_analysis(3)
    
    # Step 3: Generate comparison graph
    generate_comparison_graph()
    
    print("\n" + "=" * 60)
    print("ANALYSIS PIPELINE COMPLETED!")
    print("=" * 60)
    print("Generated files:")
    print("- results.txt (experimental data)")
    print("- theoretical_results.txt (theoretical data)")
    print("- algorithm_performance_comparison.png (comparison graph)")
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
