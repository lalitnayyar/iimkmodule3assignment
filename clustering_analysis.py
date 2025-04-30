# Required imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans  # Add this import for KMeans
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

def perform_clustering_analysis(df, features_for_clustering):
    """
    Perform K-means clustering analysis on the given features
    """
    # Standardize features for clustering
    scaler = StandardScaler()
    X_cluster = scaler.fit_transform(df[features_for_clustering])
    
    # Calculate inertia for different K values
    inertias = []
    K = range(1, 11)
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_cluster)
        inertias.append(kmeans.inertia_)
    
    # Plot elbow curve
    plt.figure(figsize=(10, 6))
    plt.plot(K, inertias, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Inertia')
    plt.title('Elbow Method For Optimal k')
    plt.show()
    
    return X_cluster, inertias

# Example usage:
# features_for_clustering = ['median_income', 'median_house_value', 'population']
# X_cluster, inertias = perform_clustering_analysis(df, features_for_clustering)
