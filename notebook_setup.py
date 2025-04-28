"""
Setup script for California Housing Analysis notebook
"""
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

def setup_notebook():
    """Configure the notebook with proper plotting settings"""
    # Ignore warnings
    warnings.filterwarnings('ignore')
    
    # Use a style that's guaranteed to exist
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Configure plot aesthetics
    plt.rcParams.update({
        'figure.figsize': (10, 6),
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'axes.grid': True,
        'grid.alpha': 0.3
    })
    
    # Set seaborn defaults
    sns.set_context("notebook")
    sns.set_palette("husl")
    
    print("✅ Notebook configured successfully with proper plotting settings")
