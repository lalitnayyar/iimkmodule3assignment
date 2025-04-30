"""
Configuration for plotting in the California Housing Analysis notebooks.
This ensures consistent and error-free plotting across environments.
"""
import matplotlib.pyplot as plt
import seaborn as sns

def setup_plotting():
    """Set up matplotlib and seaborn plotting configuration."""
    # Use a built-in matplotlib style that's guaranteed to exist
    plt.style.use('default')
    
    # Configure plot aesthetics manually
    plt.rcParams.update({
        'figure.figsize': (10, 6),
        'axes.grid': True,
        'grid.alpha': 0.3,
        'axes.labelsize': 12,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'axes.titlesize': 14,
        'figure.titlesize': 16,
        'lines.linewidth': 2,
        'axes.spines.top': False,
        'axes.spines.right': False,
    })
    
    # Set seaborn defaults
    sns.set_context("notebook")
    sns.set_palette("husl")
    
    # Return style configuration for reference
    return {
        'style': 'default',
        'context': 'notebook',
        'palette': 'husl'
    }
