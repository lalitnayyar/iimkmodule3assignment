"""
Direct fix for plotting issues in the California Housing Analysis notebook
"""
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

def configure_plots():
    """Set up plotting with guaranteed working configuration"""
    # Suppress warnings
    warnings.filterwarnings('ignore')
    
    # Reset to default style first
    plt.style.use('default')
    
    # Configure plot aesthetics manually to match seaborn style
    plt.rcParams.update({
        'figure.figsize': (10, 6),
        'axes.grid': True,
        'grid.alpha': 0.3,
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',
        'grid.color': '#b0b0b0',
        'grid.linestyle': '-',
        'grid.linewidth': 0.5,
    })
    
    # Set seaborn context and style directly
    sns.set_context("notebook")
    sns.set_style("whitegrid")
    sns.set_palette("husl")
    
    print("✅ Plotting configuration applied successfully")
