# Required imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

def clean_data(df):
    """
    Clean the data by handling missing values
    """
    # Create a copy to avoid modifying the original data
    df = df.copy()
    
    # Initialize imputer for numeric columns
    imputer = SimpleImputer(strategy='median')
    
    # Get numeric columns
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Impute missing values
    df[numeric_columns] = imputer.fit_transform(df[numeric_columns])
    
    return df

def perform_regional_analysis(df):
    """
    Perform regional analysis with proper feature scaling
    """
    # Clean the data first
    df = clean_data(df)
    
    # First, create the region feature if it doesn't exist
    # Assuming longitude < -122 is coastal
    df['region'] = np.where(df['longitude'] < -122, 'coastal', 'inland')
    
    # Select features for analysis
    features = ['median_income', 'total_rooms', 'total_bedrooms', 
               'population', 'households', 'latitude', 'longitude']
    
    # Target variable
    target = 'median_house_value'
    
    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])
    
    # Convert to DataFrame to maintain column names
    X_scaled = pd.DataFrame(X_scaled, columns=features, index=df.index)
    
    # Prepare target variable
    y = df[target]
    
    # Initialize dictionary to store results
    regional_models = {}
    regional_scores = {}
    
    # Perform analysis for each region
    for region in df['region'].unique():
        mask = df['region'] == region
        X_region = X_scaled[mask]
        y_region = y[mask]
        
        if len(X_region) > 0:  # Check if we have data for this region
            # Split the data
            X_train, X_test, y_train, y_test = train_test_split(
                X_region, y_region, test_size=0.2, random_state=42
            )
            
            # Train model
            model = LinearRegression()
            model.fit(X_train, y_train)
            
            # Store results
            regional_models[region] = model
            regional_scores[region] = regional_scores.get(region, 0) + model.score(X_test, y_test)
    
    # Print results
    print("\nRegional Analysis Results:")
    print("-------------------------")
    for region, score in regional_scores.items():
        print(f"{region.capitalize()} Region R² Score: {score:.4f}")
    
    # Visualize regional differences
    plt.figure(figsize=(12, 6))
    for region in df['region'].unique():
        mask = df['region'] == region
        plt.scatter(df[mask]['longitude'], 
                   df[mask]['median_house_value'],
                   alpha=0.5,
                   label=region)
    
    plt.xlabel('Longitude')
    plt.ylabel('Median House Value')
    plt.title('House Values by Region')
    plt.legend()
    plt.show()
    
    return regional_models, regional_scores, X_scaled

if __name__ == "__main__":
    # Load data
    print("Loading housing data...")
    df = pd.read_csv('housing.csv')
    
    # Print initial data info
    print("\nInitial data info:")
    print("------------------")
    print(f"Number of rows: {len(df)}")
    print("\nMissing values:")
    print(df.isnull().sum())
    
    print("\nPerforming regional analysis...")
    regional_models, regional_scores, X_scaled = perform_regional_analysis(df)
    
    # Print feature importance by region
    features = ['median_income', 'total_rooms', 'total_bedrooms', 
               'population', 'households', 'latitude', 'longitude']
    
    print("\nFeature importance by region:")
    for region, model in regional_models.items():
        print(f"\n{region.capitalize()} Region Feature Importance:")
        for feature, importance in zip(features, model.coef_):
            print(f"{feature}: {importance:.4f}")
