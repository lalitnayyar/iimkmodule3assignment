"""
Basic plotting configuration for matplotlib and seaborn
"""
import matplotlib.pyplot as plt
import seaborn as sns

def configure_plots():
    """Configure matplotlib and seaborn with basic settings"""
    # Reset to matplotlib defaults first
    plt.rcdefaults()
    
    # Basic matplotlib configurations
    plt.rcParams.update({
        'figure.figsize': (10, 6),
        'axes.grid': True,
        'grid.alpha': 0.3,
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'lines.linewidth': 2
    })
    
    # Basic seaborn settings without relying on style files
    sns.set_context("notebook")
    sns.set_style("whitegrid")
    
    # Return configuration for verification
    return "Plotting configured with basic matplotlib and seaborn settings"
