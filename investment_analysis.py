# Required imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler  # Add this import
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

def calculate_investment_score(df):
    # Create a copy to avoid modifying original data
    df = df.copy()
    
    # Calculate price per room
    df['price_per_room'] = df['median_house_value'] / df['total_rooms']
    
    # Calculate population density
    df['population_density'] = df['population'] / df['total_rooms']
    
    # Normalize metrics for investment score
    metrics = ['median_income', 'price_per_room', 'population_density']
    scaler = StandardScaler()
    df[['normalized_' + m for m in metrics]] = scaler.fit_transform(df[metrics])
    
    # Calculate investment score (example formula)
    df['investment_score'] = (
        df['normalized_median_income'] * 0.4 +  # Higher income areas
        -df['normalized_price_per_room'] * 0.4 +  # Lower price per room (better value)
        df['normalized_population_density'] * 0.2  # Higher population density
    )
    
    return df

# Example usage:
# df = pd.read_csv('housing.csv')
# df_with_scores = calculate_investment_score(df)
