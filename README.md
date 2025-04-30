# California Housing Prices Analysis Project

A comprehensive analysis of California housing prices with specific insights for real estate agents, property developers, and investors.

## Jupyter Notebooks Overview

All notebooks are prefixed with "LalitNayyarIIMK_" for identification. Here's a detailed overview of each notebook:

1. **`LalitNayyarIIMK_california_housing_analysis_final.ipynb`**
   - Main analysis notebook with complete implementation
   - Features comprehensive data preprocessing and cleaning
   - Includes detailed visualizations and statistical analysis
   - Contains price prediction models and evaluation
   - Best suited for end-to-end understanding of the analysis

2. **`LalitNayyarIIMK_california_housing_analysis_with_applications.ipynb`**
   - Advanced analysis with real-world applications
   - Sections include:
     - Real Estate Price Estimation
     - Regional Market Analysis (coastal vs. inland)
     - Investment Opportunity Scoring
     - Population Density Impact Studies
   - Features interactive visualizations and detailed insights
   - Recommended for business stakeholders and decision makers

3. **`LalitNayyarIIMK_california_housing_analysis_v2.ipynb`**
   - Alternative analysis approach
   - Focuses on advanced statistical methods
   - Includes experimental features and additional visualizations
   - Suitable for technical users interested in methodology

## User Guide

### Getting Started

1. **Environment Setup**
   ```bash
   # Install required packages
   pip install -r requirements.txt
   ```

2. **Launching Notebooks**
   ```bash
   # Start Jupyter Notebook
   jupyter notebook
   ```

3. **Notebook Selection**
   - For first-time users: Start with `LalitNayyarIIMK_california_housing_analysis_final.ipynb`
   - For business applications: Use `LalitNayyarIIMK_california_housing_analysis_with_applications.ipynb`
   - For advanced analysis: Explore `LalitNayyarIIMK_california_housing_analysis_v2.ipynb`

### Using the Notebooks

1. **Data Loading**
   - Each notebook automatically loads the housing dataset
   - Data is preprocessed and cleaned using standardized functions
   - Missing values are handled appropriately

2. **Navigation**
   - Use the table of contents (if available) to jump to specific sections
   - Run cells in sequence (Shift + Enter)
   - Wait for each cell to complete before running the next

3. **Visualizations**
   - Interactive plots can be zoomed and panned
   - Hover over data points for detailed information
   - Use the plot toolbar for additional options

4. **Analysis Features**
   - Price Prediction: Models for estimating house values
   - Regional Analysis: Comparison of coastal vs. inland markets
   - Investment Scoring: Automated scoring system for investment opportunities
   - Market Trends: Temporal and geographical trend analysis

### Common Tasks

1. **Updating Data**
   - Place new data in the project directory
   - Update file paths if necessary
   - Re-run the notebook from start

2. **Customizing Analysis**
   - Modify parameters in marked cells
   - Adjust visualization settings as needed
   - Update feature selection for models

3. **Exporting Results**
   - Use "File > Download as" for various formats
   - Export visualizations using the save button
   - Copy code cells for external use

### Troubleshooting

1. **Missing Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Memory Issues**
   - Restart kernel and clear output
   - Run only necessary cells
   - Reduce data size if needed

3. **Visualization Problems**
   - Ensure all plotting libraries are imported
   - Check for style conflicts
   - Reset plot parameters if needed

## Project Structure

```
iimkmodule3assignment/
├── notebooks/
│   ├── LalitNayyarIIMK_california_housing_analysis_final.ipynb
│   ├── LalitNayyarIIMK_california_housing_analysis_with_applications.ipynb
│   └── LalitNayyarIIMK_california_housing_analysis_v2.ipynb
├── utils/
│   ├── LalitNayyarIIMK_plot_fix.py
│   ├── LalitNayyarIIMK_plot_config.py
│   └── LalitNayyarIIMK_plot_config_v2.py
├── data/
│   └── housing.csv
├── requirements.txt
└── README.md
```

## Support

For any issues or questions:
1. Check the troubleshooting section
2. Review cell execution order
3. Verify data file presence and format
4. Ensure all dependencies are installed

## Version History

- v1.0: Initial release with basic analysis
- v2.0: Added advanced features and applications
- v3.0: Included regional analysis and investment scoring
