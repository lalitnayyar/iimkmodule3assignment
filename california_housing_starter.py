"""
Starter code for California Housing Analysis
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from plotting_setup import configure_plots

# Ignore warnings
warnings.filterwarnings('ignore')

# Configure plotting
configure_plots()

# Your analysis code starts here
def load_data():
    """Load and prepare the California housing dataset"""
    try:
        # Try to load the data
        df = pd.read_csv('housing.csv')
        print("Dataset loaded successfully!")
        return df
    except FileNotFoundError:
        print("Dataset not found. Please ensure 'housing.csv' is in the current directory.")
        return None

if __name__ == "__main__":
    # Load the data
    housing_data = load_data()
    
    if housing_data is not None:
        # Create a simple plot to test the configuration
        plt.figure(figsize=(10, 6))
        sns.histplot(data=housing_data, x='median_house_value', bins=50)
        plt.title('Distribution of Median House Values in California')
        plt.xlabel('Median House Value')
        plt.ylabel('Count')
        plt.show()
