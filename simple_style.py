"""
Simple and reliable plotting configuration
"""
import matplotlib.pyplot as plt
import seaborn as sns

def setup_style():
    # Use a built-in style that's guaranteed to exist
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Basic customization
    plt.rcParams.update({
        'figure.figsize': (10, 6),
        'axes.labelsize': 12,
        'axes.titlesize': 14
    })
    
    # Set seaborn defaults
    sns.set_context("notebook")
    sns.set_palette("husl")
