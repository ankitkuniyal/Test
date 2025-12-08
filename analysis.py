# analysis.py - Interactive Data Analysis Notebook
# Author: 23f2004089@ds.study.iitm.ac.in
# Research Institution Data Science Department

import marimo
__generated_with = "0.8.12"
app = marimo.App(width="full")

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Cell 1: Data Loading and Initial Processing
@app.cell
def __():
    # Load sample dataset (Iris dataset for demonstration)
    import sklearn.datasets
    
    # Load the iris dataset
    iris = sklearn.datasets.load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species_name'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    
    # Display dataset info
    print("Dataset Info:")
    print(f"Shape: {df.shape}")
    print(f"Features: {list(df.columns[:-2])}")  # Excluding species columns
    print(f"Species: {df['species_name'].unique().tolist()}")
    
    # Calculate basic statistics for demonstration
    global feature_means, feature_stds
    feature_means = df[iris.feature_names].mean().to_dict()
    feature_stds = df[iris.feature_names].std().to_dict()
    
    return df, iris, feature_means, feature_stds

# Cell 2: Interactive Slider Widget for Feature Selection
@app.cell
def __(df):
    # This cell creates an interactive slider for selecting sample size
    # The output of this widget will be used in the analysis cells
    
    import marimo as mo
    
    # Create interactive widgets
    sample_slider = mo.ui.slider(
        start=10, 
        stop=len(df), 
        step=5, 
        value=50, 
        label="Sample Size"
    )
    
    feature_dropdown = mo.ui.dropdown(
        options=['sepal length (cm)', 'sepal width (cm)', 
                'petal length (cm)', 'petal width (cm)'],
        value='petal length (cm)',
        label="Select Feature"
    )
    
    species_checkboxes = mo.ui.checkbox_group(
        options=['setosa', 'versicolor', 'virginica'],
        value=['setosa', 'versicolor', 'virginica'],
        label="Select Species"
    )
    
    # Display the widgets
    mo.md(f"""
    ## Interactive Controls
    Adjust the parameters below to explore the dataset interactively:
    
    - **Sample Size**: {sample_slider}
    - **Feature to Analyze**: {feature_dropdown}
    - **Species to Include**: {species_checkboxes}
    
    *Contact: 23f2004089@ds.study.iitm.ac.in for questions*
    """)
    
    return sample_slider, feature_dropdown, species_checkboxes, mo

# Cell 3: Data Processing with Dependencies
@app.cell
def __(df, sample_slider, species_checkboxes, feature_dropdown):
    # This cell depends on the widget states from Cell 2
    # It filters and samples the data based on user selections
    
    # Filter data based on selected species
    filtered_df = df[df['species_name'].isin(species_checkboxes.value)]
    
    # Sample data based on slider value
    sample_size = min(sample_slider.value, len(filtered_df))
    sampled_df = filtered_df.sample(n=sample_size, random_state=42)
    
    # Get the selected feature for analysis
    selected_feature = feature_dropdown.value
    
    # Calculate statistics for the selected feature
    feature_mean = sampled_df[selected_feature].mean()
    feature_median = sampled_df[selected_feature].median()
    feature_std = sampled_df[selected_feature].std()
    
    # Return processed data and statistics
    return sampled_df, selected_feature, feature_mean, feature_median, feature_std

# Cell 4: Dynamic Visualization
@app.cell
def __(sampled_df, selected_feature):
    # This cell creates visualizations based on the processed data from Cell 3
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Plot 1: Histogram of selected feature
    axes[0, 0].hist(sampled_df[selected_feature], bins=15, edgecolor='black', alpha=0.7)
    axes[0, 0].set_xlabel(selected_feature)
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].set_title(f'Distribution of {selected_feature}')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Plot 2: Box plot by species
    species_data = [sampled_df[sampled_df['species_name'] == species][selected_feature] 
                   for species in sampled_df['species_name'].unique()]
    axes[0, 1].boxplot(species_data)
    axes[0, 1].set_xticklabels(sampled_df['species_name'].unique())
    axes[0, 1].set_ylabel(selected_feature)
    axes[0, 1].set_title(f'{selected_feature} by Species')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: Scatter plot (using sepal length vs selected feature)
    colors = {'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'}
    for species in sampled_df['species_name'].unique():
        species_df = sampled_df[sampled_df['species_name'] == species]
        axes[1, 0].scatter(species_df['sepal length (cm)'], 
                          species_df[selected_feature],
                          label=species, alpha=0.6, c=colors.get(species, 'gray'))
    axes[1, 0].set_xlabel('sepal length (cm)')
    axes[1, 0].set_ylabel(selected_feature)
    axes[1, 0].set_title(f'Relationship: Sepal Length vs {selected_feature}')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Plot 4: Correlation heatmap for numerical features
    numeric_cols = ['sepal length (cm)', 'sepal width (cm)', 
                   'petal length (cm)', 'petal width (cm)']
    corr_matrix = sampled_df[numeric_cols].corr()
    im = axes[1, 1].imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1)
    axes[1, 1].set_xticks(range(len(numeric_cols)))
    axes[1, 1].set_yticks(range(len(numeric_cols)))
    axes[1, 1].set_xticklabels(numeric_cols, rotation=45)
    axes[1, 1].set_yticklabels(numeric_cols)
    axes[1, 1].set_title('Feature Correlation Matrix')
    
    # Add colorbar
    plt.colorbar(im, ax=axes[1, 1])
    
    plt.tight_layout()
    
    return fig,

# Cell 5: Dynamic Markdown Output with Statistics
@app.cell
def __(mo, sampled_df, selected_feature, feature_mean, feature_median, feature_std):
    # This cell creates dynamic markdown output based on the analysis results
    # It depends on the processed data from Cell 3
    
    # Calculate additional statistics
    feature_min = sampled_df[selected_feature].min()
    feature_max = sampled_df[selected_feature].max()
    feature_range = feature_max - feature_min
    feature_skew = sampled_df[selected_feature].skew()
    
    # Create dynamic markdown output
    analysis_report = mo.md(f"""
    ## Analysis Results
    
    ### Selected Feature: **{selected_feature}**
    
    #### Statistical Summary:
    - **Sample Size**: {len(sampled_df)} observations
    - **Mean**: {feature_mean:.3f}
    - **Median**: {feature_median:.3f}
    - **Standard Deviation**: {feature_std:.3f}
    - **Range**: {feature_min:.3f} to {feature_max:.3f} (Δ = {feature_range:.3f})
    - **Skewness**: {feature_skew:.3f} 
      ({'Right skewed' if feature_skew > 0.5 else 'Left skewed' if feature_skew < -0.5 else 'Approximately symmetric'})
    
    #### Dataset Composition:
    {sampled_df['species_name'].value_counts().to_markdown()}
    
    #### Interpretation:
    {f'The distribution shows significant variation across species.' if feature_std > 0.5 else 'The distribution is relatively tight.'}
    
    ---
    *Analysis performed by: 23f2004089@ds.study.iitm.ac.in*
    *Timestamp: {pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")}*
    """)
    
    return analysis_report,

# Cell 6: Advanced Analysis with Hypothesis Testing
@app.cell
def __(sampled_df, selected_feature, mo):
    # This cell performs hypothesis testing based on the selected data
    # Depends on sampled_df and selected_feature from Cell 3
    
    if len(sampled_df['species_name'].unique()) >= 2:
        # Perform ANOVA if we have multiple species
        species_groups = [sampled_df[sampled_df['species_name'] == species][selected_feature].values 
                         for species in sampled_df['species_name'].unique()]
        
        if all(len(group) > 1 for group in species_groups):
            # Perform one-way ANOVA
            f_stat, p_value = stats.f_oneway(*species_groups)
            
            # Create markdown with hypothesis test results
            hypothesis_test = mo.md(f"""
            ### Hypothesis Testing Results
            
            **One-Way ANOVA Test** for {selected_feature} across species:
            
            - **F-statistic**: {f_stat:.4f}
            - **P-value**: {p_value:.6f}
            - **Significance**: {'Significant difference (p < 0.05)' if p_value < 0.05 else 'No significant difference (p ≥ 0.05)'}
            
            **Interpretation**: {
                'The selected feature shows statistically significant differences between species.' 
                if p_value < 0.05 
                else 'No significant differences detected between species for this feature.'
            }
            """)
        else:
            hypothesis_test = mo.md("### Hypothesis Testing\n*Insufficient data for ANOVA test*")
    else:
        hypothesis_test = mo.md("### Hypothesis Testing\n*Need at least 2 species for comparison*")
    
    return hypothesis_test,

# Cell 7: Export and Summary
@app.cell
def __(sampled_df, mo, selected_feature):
    # Final cell with export options and summary
    # Data flow: depends on sampled_df from Cell 3
    
    # Create a download button for the sampled data
    import io
    import base64
    
    # Convert dataframe to CSV
    csv_buffer = io.StringIO()
    sampled_df.to_csv(csv_buffer, index=False)
    csv_data = csv_buffer.getvalue()
    
    # Encode for download
    b64 = base64.b64encode(csv_data.encode()).decode()
    
    summary = mo.md(f"""
    ## Summary and Export
    
    ### Analysis Complete
    
    **Feature Analyzed**: {selected_feature}
    **Total Samples**: {len(sampled_df)}
    **Unique Species**: {len(sampled_df['species_name'].unique())}
    
    ### Export Options:
    
    [Download Sampled Data as CSV](data:text/csv;base64,{b64} "sampled_data.csv")
    
    ### Next Steps:
    1. Review the statistical summary above
    2. Examine the visualizations for patterns
    3. Consider the hypothesis test results
    4. Download data for further analysis
    
    ---
    **Notebook Features Demonstrated:**
    - ✅ Interactive widgets (slider, dropdown, checkboxes)
    - ✅ Dynamic data filtering and sampling
    - ✅ Real-time visualization updates
    - ✅ Statistical analysis with hypothesis testing
    - ✅ Self-documenting markdown output
    
    *For reproducibility, this notebook maintains clear data flow between cells.*
    """)
    
    return summary,

if __name__ == "__main__":
    app.run()