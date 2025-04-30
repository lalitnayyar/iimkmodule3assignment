# Cell 1: Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler  # This is the missing import
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Print available styles and then set up plotting
print("Available styles:", plt.style.available)
plt.style.use('seaborn-v0_8')
sns.set_context("notebook")

# Cell 2: Load and prepare data
# Make sure your housing.csv file is in the correct location
df = pd.read_csv('housing.csv')

# Cell 3: Calculate investment metrics
# Create price per room and population density features
df['price_per_room'] = df['median_house_value'] / df['total_rooms']
df['population_density'] = df['population'] / df['total_rooms']

# Normalize metrics for investment score
metrics = ['median_income', 'price_per_room', 'population_density']
scaler = StandardScaler()
df[['normalized_' + m for m in metrics]] = scaler.fit_transform(df[metrics])

# Calculate investment score
df['investment_score'] = (
    df['normalized_median_income'] * 0.4 +  # Higher income areas
    -df['normalized_price_per_room'] * 0.4 +  # Lower price per room (better value)
    df['normalized_population_density'] * 0.2  # Higher population density
)
