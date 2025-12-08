"""
Professional Marketing Campaign Analysis Visualization
Author: 23f2004089@ds.study.iitm.ac.in
Date: November 2024
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_marketing_data(n_samples=200):
    """
    Generate realistic synthetic marketing campaign data.
    
    Parameters:
    -----------
    n_samples : int
        Number of data points to generate
        
    Returns:
    --------
    pandas.DataFrame
        DataFrame containing marketing campaign metrics
    """
    np.random.seed(42)  # For reproducibility
    
    # Campaign types with different characteristics
    campaign_types = ['Digital', 'Social Media', 'Email', 'TV']
    
    # Generate synthetic data for each campaign type
    data = []
    
    for campaign_type in campaign_types:
        n_campaign = n_samples // 4
        
        if campaign_type == 'Digital':
            # Digital campaigns: moderate spend, high conversion
            spend = np.random.normal(40, 10, n_campaign)
            conversion = np.random.normal(8.5, 1.5, n_campaign)
            engagement = np.random.normal(7.5, 1.2, n_campaign)
        elif campaign_type == 'Social Media':
            # Social media: lower spend, variable conversion
            spend = np.random.normal(25, 8, n_campaign)
            conversion = np.random.normal(7.0, 2.0, n_campaign)
            engagement = np.random.normal(8.0, 1.0, n_campaign)
        elif campaign_type == 'Email':
            # Email: low spend, moderate conversion
            spend = np.random.normal(15, 5, n_campaign)
            conversion = np.random.normal(6.5, 1.0, n_campaign)
            engagement = np.random.normal(6.0, 1.5, n_campaign)
        else:  # TV
            # TV: high spend, variable conversion
            spend = np.random.normal(75, 20, n_campaign)
            conversion = np.random.normal(5.5, 2.5, n_campaign)
            engagement = np.random.normal(5.0, 1.8, n_campaign)
        
        # Ensure positive values and realistic ranges
        spend = np.clip(spend, 5, 150)
        conversion = np.clip(conversion, 1, 15)
        engagement = np.clip(engagement, 1, 10)
        
        # Add ROI (Return on Investment) as a derived metric
        roi = (conversion * 1000 - spend * 10) / (spend * 10) * 100
        
        # Create data for this campaign type
        for i in range(n_campaign):
            data.append({
                'Campaign_Type': campaign_type,
                'Marketing_Spend_K': round(spend[i], 2),
                'Conversion_Rate': round(conversion[i], 2),
                'Engagement_Score': round(engagement[i], 2),
                'ROI_Percent': round(roi[i], 2),
                'Customer_Segment': np.random.choice(['New', 'Returning', 'Premium'], 
                                                    p=[0.5, 0.3, 0.2])
            })
    
    return pd.DataFrame(data)

def create_marketing_scatterplot(df):
    """
    Create a professional scatterplot for marketing campaign analysis.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing marketing data
        
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    # Set professional Seaborn styling
    sns.set_style("whitegrid")
    sns.set_context("notebook", font_scale=1.2)
    
    # Create figure with square dimensions for 512x512 output
    plt.figure(figsize=(8, 8))
    
    # Define custom color palette for campaign types
    campaign_palette = {
        'Digital': '#2E86AB',      # Professional blue
        'Social Media': '#A23B72',  # Modern magenta
        'Email': '#F18F01',         # Attention-grabbing orange
        'TV': '#C73E1D'            # Bold red
    }
    
    # Create scatterplot with enhanced aesthetics
    scatter = sns.scatterplot(
        data=df,
        x='Marketing_Spend_K',
        y='Conversion_Rate',
        hue='Campaign_Type',
        size='Engagement_Score',
        sizes=(50, 300),  # Range of bubble sizes
        alpha=0.7,
        edgecolor='black',
        linewidth=0.5,
        palette=campaign_palette,
        legend='full'
    )
    
    # Customize the plot appearance
    plt.title(
        'Marketing Campaign Effectiveness Analysis\n' +
        'Spend vs. Conversion Rate by Campaign Type',
        fontsize=16,
        fontweight='bold',
        pad=20
    )
    
    plt.xlabel(
        'Marketing Spend (Thousands of Dollars)',
        fontsize=13,
        fontweight='medium'
    )
    
    plt.ylabel(
        'Conversion Rate (%)',
        fontsize=13,
        fontweight='medium'
    )
    
    # Add grid for better readability
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # Customize legend
    legend = plt.legend(
        title='Campaign Type',
        title_fontsize='12',
        fontsize='11',
        loc='upper right',
        frameon=True,
        framealpha=0.9,
        edgecolor='black'
    )
    
    # Adjust legend for bubble sizes
    legend.get_frame().set_linewidth(1)
    
    # Add annotation for key insight
    plt.annotate(
        'Digital campaigns show\noptimal spend-to-conversion ratio',
        xy=(45, 8.5),
        xytext=(60, 11),
        arrowprops=dict(
            arrowstyle='->',
            color='#2E86AB',
            lw=2
        ),
        fontsize=11,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#2E86AB", alpha=0.1)
    )
    
    # Add a trend line for Digital campaigns
    digital_df = df[df['Campaign_Type'] == 'Digital']
    if len(digital_df) > 1:
        z = np.polyfit(digital_df['Marketing_Spend_K'], 
                      digital_df['Conversion_Rate'], 1)
        p = np.poly1d(z)
        plt.plot(digital_df['Marketing_Spend_K'], 
                p(digital_df['Marketing_Spend_K']),
                color='#2E86AB',
                linestyle='--',
                alpha=0.5,
                label='Digital Trend')
    
    # Set axis limits for better visualization
    plt.xlim(0, 160)
    plt.ylim(0, 16)
    
    # Add subtle background color
    plt.gca().set_facecolor('#F8F9FA')
    
    # Tight layout for better spacing
    plt.tight_layout()
    
    return plt.gcf()

def main():
    """Main function to generate and save the visualization."""
    print("Generating marketing campaign data...")
    df = generate_marketing_data()
    
    print(f"Generated {len(df)} data points")
    print(f"Campaign types: {df['Campaign_Type'].unique().tolist()}")
    print(f"Spend range: ${df['Marketing_Spend_K'].min():.2f}K - ${df['Marketing_Spend_K'].max():.2f}K")
    print(f"Conversion range: {df['Conversion_Rate'].min():.2f}% - {df['Conversion_Rate'].max():.2f}%")
    
    print("\nCreating professional scatterplot...")
    fig = create_marketing_scatterplot(df)
    
    # Save the figure with exact 512x512 pixel dimensions
    # dpi=64 with 8x8 inches gives 512x512 (64 * 8 = 512)
    print("\nSaving chart as 'chart.png' (512x512 pixels)...")
    fig.savefig(
        'chart.png',
        dpi=64,  # 64 DPI × 8 inches = 512 pixels
        bbox_inches='tight',
        facecolor='white',
        edgecolor='none'
    )
    
    # Verify the output dimensions
    from PIL import Image
    img = Image.open('chart.png')
    width, height = img.size
    print(f"Saved image dimensions: {width}×{height} pixels")
    
    if width == 512 and height == 512:
        print("✓ Successfully created 512×512 pixel visualization!")
    else:
        print(f"✗ Warning: Image dimensions are {width}×{height}, expected 512×512")
    
    # Display summary statistics
    print("\n=== Campaign Performance Summary ===")
    summary = df.groupby('Campaign_Type').agg({
        'Marketing_Spend_K': ['mean', 'std'],
        'Conversion_Rate': ['mean', 'std'],
        'Engagement_Score': 'mean'
    }).round(2)
    
    print(summary)
    
    print("\nVisualization saved successfully!")
    print("Contact: 23f2004089@ds.study.iitm.ac.in")

if __name__ == "__main__":
    main()