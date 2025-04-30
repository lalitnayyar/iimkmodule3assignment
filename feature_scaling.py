# Required imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

def prepare_scaled_features(df, features_to_scale):
    """
    Scale features using StandardScaler
    """
    # Initialize the scaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    X_scaled = scaler.fit_transform(df[features_to_scale])
    
    # Convert to DataFrame to maintain column names
    X_scaled = pd.DataFrame(X_scaled, columns=features_to_scale, index=df.index)
    
    return X_scaled

def perform_clustering_analysis(df):
    # Select features for clustering
    features_to_scale = ['median_income', 'median_house_value', 'population', 
                        'total_rooms', 'total_bedrooms', 'households']
    
    # Scale the features
    X_scaled = prepare_scaled_features(df, features_to_scale)
    
    # Perform clustering
    inertias = []
    K = range(1, 11)
    
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        inertias.append(kmeans.inertia_)
    
    # Plot elbow curve
    plt.figure(figsize=(10, 6))
    plt.plot(K, inertias, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Inertia')
    plt.title('Elbow Method For Optimal k')
    plt.show()
    
    # Choose optimal k (for example, k=4)
    optimal_k = 4
    kmeans = KMeans(n_clusters=optimal_k, random_state=42)
    df['cluster'] = kmeans.fit_predict(X_scaled)
    
    return df, X_scaled

# Example usage in notebook:
"""
# Load data
df = pd.read_csv('housing.csv')

# Perform clustering analysis
df, X_scaled = perform_clustering_analysis(df)

# Now you can use X_scaled for further analysis
print("Shape of scaled features:", X_scaled.shape)
print("\nFirst few rows of scaled features:")
print(X_scaled.head())
"""
