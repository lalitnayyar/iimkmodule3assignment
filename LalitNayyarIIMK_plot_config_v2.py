"""
Updated plotting configuration for California Housing Analysis
"""
import matplotlib.pyplot as plt
import seaborn as sns

def setup_plots():
    """Configure plotting with a style that's guaranteed to work"""
    # Use seaborn-v0_8-whitegrid style which is available
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Additional customization
    plt.rcParams.update({
        'figure.figsize': (10, 6),
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10
    })
    
    # Set seaborn context and palette
    sns.set_context("notebook")
    sns.set_palette("husl")
    
    return "Plotting configured successfully"

# Test the configuration
if __name__ == "__main__":
    import numpy as np
    
    setup_plots()
    
    # Create a test plot
    x = np.linspace(0, 10, 100)
    plt.figure()
    plt.plot(x, np.sin(x))
    plt.title("Test Plot")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()
