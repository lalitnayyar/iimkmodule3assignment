# California Housing Prices Analysis Project

A comprehensive analysis of California housing prices with specific insights for real estate agents, property developers, and investors.

## Available Notebooks

1. **california_housing_analysis_final.ipynb**
   - Main analysis notebook with complete implementation
   - Includes data preprocessing, visualization, and modeling
   - Uses robust plotting configuration
   - Best for end-to-end analysis

2. **california_housing_analysis_with_applications.ipynb**
   - Extended analysis with real-world applications
   - Specific sections for:
     - Real Estate Agent Analysis
     - Property Developer Analysis
     - Investment Opportunities
   - Enhanced visualizations and market insights

3. **california_housing_analysis_v2.ipynb**
   - Updated version with improved plotting configuration
   - Fixed style-related issues
   - Enhanced data visualization
   - Optimized code structure

4. **california_housing_analysis_fixed.ipynb**
   - Version with basic plotting fixes
   - Simplified analysis workflow
   - Good starting point for beginners

## Setup Instructions

1. Install required packages:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn kaggle folium --upgrade
   ```

2. Set up Kaggle credentials:
   - Go to kaggle.com → Account → Create API Token
   - Download `kaggle.json`
   - Place in:
     - Windows: `C:\Users\<username>\.kaggle\kaggle.json`
     - Linux/Mac: `~/.kaggle/kaggle.json`

3. Clone this repository:
   ```bash
   git clone https://github.com/lalitnayyar/iimkmodule3assignment.git
   cd iimkmodule3assignment
   ```

## User Guide

### Getting Started
1. Start with `california_housing_analysis_final.ipynb`
2. Run cells in sequence
3. Dataset will be downloaded automatically

### Notebook Features

#### Data Analysis
- Data loading and preprocessing
- Missing value handling
- Feature engineering
- Statistical analysis

#### Visualizations
- Price distribution maps
- Location-based analysis
- Market segment visualization
- Trend analysis charts

#### Models and Predictions
- Linear regression
- Price prediction models
- Market segmentation
- Investment scoring

### Stakeholder-Specific Insights

1. **For Real Estate Agents**
   - Regional price trends
   - Neighborhood analysis
   - Price prediction tools
   - Client recommendation features

2. **For Property Developers**
   - Land value analysis
   - Development opportunity scoring
   - Population density insights
   - Growth potential metrics

3. **For Investors**
   - ROI predictions
   - Market timing analysis
   - Risk assessment tools
   - Portfolio optimization

## Troubleshooting

### Common Issues

1. **Plotting Issues**
   - Use the provided `plot_fix.py` configuration
   - Import with: `from plot_fix import configure_plots`
   - Run `configure_plots()` before creating visualizations

2. **Data Loading Issues**
   - Ensure `housing.csv` is in the project directory
   - Check Kaggle API credentials if using automatic download

3. **Package Issues**
   - Run `pip install -r requirements.txt`
   - Ensure all dependencies are up to date

### Getting Help
- Check the [GitHub Issues](https://github.com/lalitnayyar/iimkmodule3assignment/issues)
- Review notebook comments for specific guidance
- Use provided helper functions in utility files

## Project Structure

```
iimkmodule3assignment/
├── notebooks/
│   ├── california_housing_analysis_final.ipynb
│   ├── california_housing_analysis_with_applications.ipynb
│   ├── california_housing_analysis_v2.ipynb
│   └── california_housing_analysis_fixed.ipynb
├── utils/
│   ├── plot_fix.py
│   ├── plot_config.py
│   └── notebook_setup.py
├── data/
│   └── housing.csv
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
