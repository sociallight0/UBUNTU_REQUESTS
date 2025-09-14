#!/usr/bin/env python3
"""
Matplotlib Line Graph Demonstrations
Various types of line graphs and plotting techniques
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

def basic_line_graph():
    """Create a basic line graph"""
    print("Creating basic line graph...")
    
    # Simple data
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', linewidth=2, markersize=6)
    plt.title('Basic Line Graph - Linear Growth')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.grid(True, alpha=0.3)
    plt.show()

def multiple_lines():
    """Create graph with multiple lines"""
    print("Creating multiple line graph...")
    
    x = np.linspace(0, 10, 50)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) * np.cos(x)
    
    plt.figure(figsize=(12, 8))
    plt.plot(x, y1, label='sin(x)', linewidth=2, color='blue')
    plt.plot(x, y2, label='cos(x)', linewidth=2, color='red')
    plt.plot(x, y3, label='sin(x) * cos(x)', linewidth=2, color='green')
    
    plt.title('Multiple Line Graph - Trigonometric Functions')
    plt.xlabel('X Values (radians)')
    plt.ylabel('Y Values')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

def styled_line_graph():
    """Create a styled line graph with different line styles"""
    print("Creating styled line graph...")
    
    x = np.linspace(0, 20, 100)
    y1 = np.exp(-x/10) * np.cos(x)
    y2 = np.exp(-x/10) * np.sin(x)
    y3 = np.exp(-x/10)
    y4 = -np.exp(-x/10)
    
    plt.figure(figsize=(14, 8))
    
    plt.plot(x, y1, '--', label='Damped Cosine', linewidth=2, color='purple')
    plt.plot(x, y2, '-.', label='Damped Sine', linewidth=2, color='orange')
    plt.plot(x, y3, ':', label='Exponential Decay', linewidth=3, color='red')
    plt.plot(x, y4, ':', linewidth=3, color='red', alpha=0.7)
    
    plt.title('Styled Line Graph - Damped Oscillations', fontsize=16, fontweight='bold')
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Amplitude', fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    # Add shaded region
    plt.fill_between(x, y3, y4, alpha=0.2, color='red', label='Envelope')
    
    plt.tight_layout()
    plt.show()

def time_series_graph():
    """Create a time series line graph"""
    print("Creating time series graph...")
    
    # Generate time data
    start_date = datetime(2024, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(365)]
    
    # Generate sample data (temperature over year)
    np.random.seed(42)
    base_temp = 20 + 15 * np.sin(2 * np.pi * np.arange(365) / 365)  # Seasonal variation
    daily_variation = np.random.normal(0, 3, 365)  # Daily randomness
    temperatures = base_temp + daily_variation
    
    plt.figure(figsize=(15, 8))
    plt.plot(dates, temperatures, linewidth=1, color='steelblue', alpha=0.7)
    
    # Add trend line
    z = np.polyfit(range(365), temperatures, 1)
    p = np.poly1d(z)
    plt.plot(dates, p(range(365)), "r--", linewidth=2, label=f'Trend: {z[0]:.3f}°C/day')
    
    plt.title('Time Series - Daily Temperature Throughout 2024', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Format x-axis
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def subplot_line_graphs():
    """Create multiple subplots with different line graphs"""
    print("Creating subplot line graphs...")
    
    # Data for different plots
    x = np.linspace(0, 10, 100)
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Plot 1: Polynomial functions
    axes[0, 0].plot(x, x**2, label='x²', linewidth=2)
    axes[0, 0].plot(x, x**3/10, label='x³/10', linewidth=2)
    axes[0, 0].set_title('Polynomial Functions')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # Plot 2: Exponential functions
    axes[0, 1].plot(x, np.exp(x/5), label='e^(x/5)', linewidth=2, color='red')
    axes[0, 1].plot(x, np.log(x + 1), label='ln(x+1)', linewidth=2, color='green')
    axes[0, 1].set_title('Exponential and Logarithmic')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: Random walk
    np.random.seed(42)
    steps = np.random.choice([-1, 1], size=100)
    walk = np.cumsum(steps)
    axes[1, 0].plot(range(100), walk, linewidth=2, color='purple')
    axes[1, 0].set_title('Random Walk')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Plot 4: Stock-like data
    np.random.seed(42)
    price = 100
    prices = [price]
    for _ in range(99):
        price *= (1 + np.random.normal(0, 0.02))
        prices.append(price)
    
    axes[1, 1].plot(range(100), prices, linewidth=2, color='darkgreen')
    axes
