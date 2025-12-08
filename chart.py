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
    
    # Create figure with EXACT dimensions for 512x512 output
    # Using figsize=(6.4, 6.4) and dpi=80 gives exactly 512x512
    fig = plt.figure(figsize=(6.4, 6.4), dpi=80, facecolor='white')
    
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
        sizes=(30, 200),  # Smaller range for square format
        alpha=0.7,
        edgecolor='black',
        linewidth=0.5,
        palette=campaign_palette,
        legend='full'
    )
    
    # Customize the plot appearance
    plt.title(
        'Marketing Campaign Effectiveness\nSpend vs. Conversion Rate',
        fontsize=14,
        fontweight='bold',
        pad=15
    )
    
    plt.xlabel(
        'Marketing Spend (Thousands $)',
        fontsize=12,
        fontweight='medium'
    )
    
    plt.ylabel(
        'Conversion Rate (%)',
        fontsize=12,
        fontweight='medium'
    )
    
    # Add grid for better readability
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # Customize legend - position it better for square format
    legend = plt.legend(
        title='Campaign Type',
        title_fontsize='11',
        fontsize='10',
        loc='upper left',
        bbox_to_anchor=(1.02, 1),  # Move legend outside plot
        borderaxespad=0.,
        frameon=True,
        framealpha=0.9,
        edgecolor='black'
    )
    
    # Adjust legend for bubble sizes
    legend.get_frame().set_linewidth(1)
    
    # Add annotation for key insight
    plt.annotate(
        'Digital: Optimal ROI',
        xy=(45, 8.5),
        xytext=(70, 10),
        arrowprops=dict(
            arrowstyle='->',
            color='#2E86AB',
            lw=1.5
        ),
        fontsize=10,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#2E86AB", alpha=0.1)
    )
    
    # Set axis limits for better visualization
    plt.xlim(0, 160)
    plt.ylim(0, 16)
    
    # Adjust layout to make room for legend
    plt.subplots_adjust(right=0.75)  # Make space for legend on the right
    
    return fig

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
    print("\nSaving chart as 'chart.png' (512x512 pixels)...")
    
    # Method 1: Save with exact dimensions
    # Remove bbox_inches='tight' to maintain exact size
    fig.savefig(
        'chart.png',
        dpi=80,  # 80 DPI × 6.4 inches = 512 pixels
        bbox_inches=None,  # Do NOT use tight bounding box
        pad_inches=0.1,    # Small padding instead
        facecolor='white',
        edgecolor='none'
    )
    
    # Alternative method using set_size_inches
    fig.set_size_inches(6.4, 6.4)  # Exactly 6.4 inches
    
    # Save again with exact dimensions
    fig.savefig(
        'chart.png',
        dpi=80,
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
        print(f"✗ Image dimensions are {width}×{height}, trying alternative method...")
        
        # Force exact dimensions using PIL
        img = Image.open('chart.png')
        img_resized = img.resize((512, 512), Image.Resampling.LANCZOS)
        img_resized.save('chart.png')
        
        # Verify again
        img_final = Image.open('chart.png')
        width_final, height_final = img_final.size
        print(f"Final image dimensions: {width_final}×{height_final} pixels")
        
        if width_final == 512 and height_final == 512:
            print("✓ Successfully resized to 512×512 pixels!")
        else:
            print("✗ Could not achieve 512×512 dimensions")
    
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