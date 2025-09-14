#!/usr/bin/env python3
"""
NumPy Demonstration
Working with arrays, mathematical operations, and data manipulation
"""

import numpy as np
import matplotlib.pyplot as plt

def basic_array_operations():
    """Demonstrate basic NumPy array operations"""
    print("=== NumPy Array Operations ===")
    
    # Create arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.arange(1, 11)  # 1 to 10
    arr3 = np.linspace(0, 10, 5)  # 5 points from 0 to 10
    
    print(f"Array 1: {arr1}")
    print(f"Array 2 (1-10): {arr2}")
    print(f"Array 3 (linspace): {arr3}")
    
    # Mathematical operations
    print(f"\nMean of arr2: {np.mean(arr2)}")
    print(f"Standard deviation: {np.std(arr2):.2f}")
    print(f"Sum: {np.sum(arr2)}")
    print(f"Max: {np.max(arr2)}, Min: {np.min(arr2)}")
    
    return arr2

def matrix_operations():
    """Demonstrate 2D array/matrix operations"""
    print("\n=== Matrix Operations ===")
    
    # Create 2D arrays
    matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
    matrix2 = np.random.randint(1, 10, (3, 2))
    
    print(f"Matrix 1:\n{matrix1}")
    print(f"Matrix 2:\n{matrix2}")
    
    # Matrix multiplication
    result = np.dot(matrix1, matrix2)
    print(f"Matrix multiplication result:\n{result}")
    
    # Other operations
    print(f"Matrix 1 shape: {matrix1.shape}")
    print(f"Matrix 1 transposed:\n{matrix1.T}")

def statistical_analysis():
    """Demonstrate statistical operations"""
    print("\n=== Statistical Analysis ===")
    
    # Generate random data
    np.random.seed(42)  # For reproducibility
    data = np.random.normal(100, 15, 1000)  # Normal distribution
    
    print(f"Dataset size: {len(data)}")
    print(f"Mean: {np.mean(data):.2f}")
    print(f"Median: {np.median(data):.2f}")
    print(f"Standard deviation: {np.std(data):.2f}")
    print(f"25th percentile: {np.percentile(data, 25):.2f}")
    print(f"75th percentile: {np.percentile(data, 75):.2f}")
    
    return data

def array_manipulation():
    """Demonstrate array reshaping and manipulation"""
    print("\n=== Array Manipulation ===")
    
    # Create and reshape arrays
    arr = np.arange(12)
    print(f"Original array: {arr}")
    
    reshaped = arr.reshape(3, 4)
    print(f"Reshaped to 3x4:\n{reshaped}")
    
    # Indexing and slicing
    print(f"First row: {reshaped[0, :]}")
    print(f"Last column: {reshaped[:, -1]}")
    print(f"Elements > 6: {arr[arr > 6]}")

def main():
    """Main function to run all demonstrations"""
    print("NumPy Library Demonstration")
    print("=" * 40)
    
    data = basic_array_operations()
    matrix_operations()
    statistical_data = statistical_analysis()
    array_manipulation()
    
    # Simple visualization
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(data)
    plt.title('Array Values')
    plt.xlabel('Index')
    plt.ylabel('Value')
    
    plt.subplot(1, 2, 2)
    plt.hist(statistical_data, bins=30, alpha=0.7)
    plt.title('Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()
    
    print("\nNumPy demonstration completed!")

if __name__ == "__main__":
    main()
