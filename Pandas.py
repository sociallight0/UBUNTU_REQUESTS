#!/usr/bin/env python3
"""
Pandas Demonstration
Data manipulation, analysis, and CSV handling
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_sample_data():
    """Create sample data for demonstration"""
    print("=== Creating Sample Dataset ===")
    
    # Create sample employee data
    np.random.seed(42)
    n_employees = 100
    
    data = {
        'employee_id': range(1, n_employees + 1),
        'name': [f'Employee_{i}' for i in range(1, n_employees + 1)],
        'department': np.random.choice(['IT', 'Finance', 'HR', 'Marketing', 'Sales'], n_employees),
        'age': np.random.randint(22, 65, n_employees),
        'salary': np.random.normal(60000, 15000, n_employees).astype(int),
        'years_experience': np.random.randint(0, 20, n_employees),
        'performance_rating': np.random.choice(['Poor', 'Average', 'Good', 'Excellent'], 
                                             n_employees, p=[0.1, 0.3, 0.4, 0.2])
    }
    
    df = pd.DataFrame(data)
    print(f"Created dataset with {len(df)} employees")
    print(f"Columns: {list(df.columns)}")
    
    return df

def basic_dataframe_operations(df):
    """Demonstrate basic DataFrame operations"""
    print("\n=== Basic DataFrame Operations ===")
    
    # Display basic info
    print("First 5 rows:")
    print(df.head())
    
    print(f"\nDataFrame shape: {df.shape}")
    print(f"Data types:\n{df.dtypes}")
    
    print("\nSummary statistics:")
    print(df.describe())
    
    # Basic filtering
    it_employees = df[df['department'] == 'IT']
    print(f"\nIT employees: {len(it_employees)}")
    
    high_earners = df[df['salary'] > 70000]
    print(f"Employees earning > $70k: {len(high_earners)}")

def data_analysis_operations(df):
    """Demonstrate data analysis operations"""
    print("\n=== Data Analysis Operations ===")
    
    # Group by operations
    dept_stats = df.groupby('department').agg({
        'salary': ['mean', 'min', 'max', 'count'],
        'age': 'mean',
        'years_experience': 'mean'
    }).round(2)
    
    print("Department statistics:")
    print(dept_stats)
    
    # Value counts
    print(f"\nDepartment distribution:")
    print(df['department'].value_counts())
    
    print(f"\nPerformance rating distribution:")
    print(df['performance_rating'].value_counts())
    
    # Correlation analysis
    print(f"\nCorrelation between salary and experience:")
    correlation = df['salary'].corr(df['years_experience'])
    print(f"{correlation:.3f}")

def data_manipulation(df):
    """Demonstrate data manipulation techniques"""
    print("\n=== Data Manipulation ===")
    
    # Create new columns
    df['salary_category'] = pd.cut(df['salary'], 
                                  bins=[0, 50000, 65000, 80000, float('inf')],
                                  labels=['Low', 'Medium', 'High', 'Very High'])
    
    df['age_group'] = pd.cut(df['age'], 
                            bins=[0, 30, 45, 65],
                            labels=['Young', 'Middle', 'Senior'])
    
    print("Added new categorical columns:")
    print(df[['name', 'salary', 'salary_category', 'age', 'age_group']].head())
    
    # Sorting and ranking
    top_earners = df.nlargest(5, 'salary')[['name', 'department', 'salary']]
    print(f"\nTop 5 earners:")
    print(top_earners)

def save_and_load_csv(df):
    """Demonstrate CSV operations"""
    print("\n=== CSV Operations ===")
    
    # Save to CSV
    filename = 'employee_data.csv'
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
    
    # Load from CSV
    loaded_df = pd.read_csv(filename)
    print(f"Loaded data shape: {loaded_df.shape}")
    
    # Show first few rows of loaded data
    print("First 3 rows of loaded data:")
    print(loaded_df.head(3))
    
    return loaded_df

def data_visualization(df):
    """Create visualizations using pandas plotting"""
    print("\n=== Data Visualization ===")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Salary distribution
    df['salary'].hist(bins=20, ax=axes[0,0])
    axes[0,0].set_title('Salary Distribution')
    axes[0,0].set_xlabel('Salary')
    axes[0,0].set_ylabel('Frequency')
    
    # Department counts
    df['department'].value_counts().plot(kind='bar', ax=axes[0,1])
    axes[0,1].set_title('Employee Count by Department')
    axes[0,1].set_xlabel('Department')
    axes[0,1].set_ylabel('Count')
    
    # Salary vs Experience scatter plot
    df.plot.scatter(x='years_experience', y='salary', ax=axes[1,0])
    axes[1,0].set_title('Salary vs Years of Experience')
    
    # Performance rating pie chart
    df['performance_rating'].value_counts().plot(kind='pie', ax=axes[1,1])
    axes[1,1].set_title('Performance Rating Distribution')
    
    plt.tight_layout()
    plt.show()

def advanced_operations(df):
    """Demonstrate advanced pandas operations"""
    print("\n=== Advanced Operations ===")
    
    # Pivot table
    pivot = df.pivot_table(
        values='salary',
        index='department',
        columns='performance_rating',
        aggfunc='mean',
        fill_value=0
    ).round(0)
    
    print("Salary pivot table (Department vs Performance):")
    print(pivot)
    
    # Missing data handling (artificially create some)
    df_copy = df.copy()
    df_copy.loc[0:5, 'salary'] = np.nan
    
    print(f"\nMissing values created: {df_copy['salary'].isna().sum()}")
    print("Filling missing values with department mean...")
    
    df_copy['salary'] = df_copy.groupby('department')['salary'].transform(
        lambda x: x.fillna(x.mean())
    )
    
    print(f"Missing values after filling: {df_copy['salary'].isna().sum()}")

def main():
    """Main function to run all demonstrations"""
    print("Pandas Library Demonstration")
    print("=" * 40)
    
    # Create and work with data
    df = create_sample_data()
    basic_dataframe_operations(df)
    data_analysis_operations(df)
    data_manipulation(df)
    loaded_df = save_and_load_csv(df)
    data_visualization(df)
    advanced_operations(df)
    
    print("\nPandas demonstration completed!")
    print("Check the 'employee_data.csv' file created in your directory.")

if __name__ == "__main__":
    main()
