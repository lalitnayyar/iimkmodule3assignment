# California Housing Prices Analysis

This project analyzes the California Housing Prices dataset to build and evaluate prediction models, with specific focus on insights for real estate agents, property developers, and investors.

## Setup Instructions

1. Install Python packages first:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn kaggle folium --upgrade
   ```

2. Set up Kaggle API credentials:
   - Go to your Kaggle account settings (https://www.kaggle.com/account)
   - Click on "Create New API Token" to download `kaggle.json`
   - Place the `kaggle.json` file in:
     - Windows: `C:\Users\<Windows-username>\.kaggle\kaggle.json`
     - Linux/Mac: `~/.kaggle/kaggle.json`

3. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

4. Open `california_housing_analysis_v2.ipynb` and run the cells in sequence
   - The notebook uses a custom plotting configuration that works across all environments
   - No style-related errors will occur
   - The dataset will be downloaded automatically when you run the notebook

## Project Structure

- `california_housing_analysis_v2.ipynb`: Main analysis notebook with robust plotting configuration
- `requirements.txt`: Python package dependencies
- `housing.csv`: Dataset (downloaded automatically by the notebook)

## Analysis Sections

### 1. Real Estate Agent Analysis
- Regional price distribution analysis with custom visualizations
- Local market factor visualization using matplotlib's native plotting
- Price prediction models by region
- Market dynamics charts

### 2. Property Developer Analysis
- Market segmentation analysis
- Population density heat maps
- Development potential scoring
- Income level distribution

### 3. Investor Analysis
- Investment opportunity heat maps
- Growth potential metrics
- Income trend analysis
- ROI prediction models

## Features

1. **Robust Visualization Setup**
   - Custom plotting configuration that works everywhere
   - No dependency on external style files
   - Consistent appearance across different environments

2. **Automated Data Handling**
   - Automatic dataset download via Kaggle API
   - Fallback to manual download if needed
   - Built-in data preprocessing

3. **Comprehensive Analysis**
   - Region-specific insights
   - Market segmentation
   - Investment scoring
   - Growth potential analysis

## Troubleshooting

If you encounter any issues:
1. Make sure all packages are up to date using the install command above
2. The notebook uses a custom plotting setup that avoids any style-related errors
3. If you can't download the dataset automatically, use the manual download link provided in the notebook
