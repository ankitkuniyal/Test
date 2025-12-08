"""
Employee Department Analysis
Author: 23f2004089@ds.study.iitm.ac.in
Date: December 2024
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

def create_sample_data():
    """Create a realistic sample employee dataset."""
    np.random.seed(42)
    
    departments = ['IT', 'HR', 'Finance', 'Marketing', 'Operations', 'Sales', 'IT', 
                   'IT', 'HR', 'Finance', 'IT', 'Marketing', 'IT', 'Operations', 
                   'Sales', 'IT', 'HR', 'Finance', 'Marketing', 'IT', 'Operations', 
                   'Sales', 'IT', 'HR', 'IT']
    
    data = {
        'Employee_ID': range(1001, 1001 + len(departments)),
        'Name': [f'Employee_{i}' for i in range(len(departments))],
        'Department': departments,
        'Salary': np.random.normal(60000, 15000, len(departments)),
        'Years_Experience': np.random.randint(1, 20, len(departments))
    }
    
    return pd.DataFrame(data)

def analyze_departments(df):
    """Analyze department frequencies and create visualization."""
    
    print("=" * 60)
    print("EMPLOYEE DEPARTMENT ANALYSIS")
    print("=" * 60)
    print(f"Analysis by: 23f2004089@ds.study.iitm.ac.in\n")
    
    # 1. Calculate frequency count for IT department
    it_count = df[df['Department'] == 'IT'].shape[0]
    total_employees = df.shape[0]
    it_percentage = (it_count / total_employees) * 100
    
    print("DEPARTMENT FREQUENCY ANALYSIS:")
    print("-" * 40)
    print(f"Total Employees: {total_employees}")
    print(f"IT Department Count: {it_count}")
    print(f"IT Department Percentage: {it_percentage:.1f}%")
    print()
    
    # 2. Calculate frequency for all departments
    dept_counts = df['Department'].value_counts()
    print("DEPARTMENT DISTRIBUTION:")
    print("-" * 40)
    print(dept_counts)
    print()
    
    # 3. Create histogram visualization
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Bar chart - Department Distribution
    colors = ['#2E86AB' if dept == 'IT' else '#A23B72' for dept in dept_counts.index]
    bars = ax1.bar(dept_counts.index, dept_counts.values, color=colors, edgecolor='black')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{int(height)}', ha='center', va='bottom', fontweight='bold')
    
    ax1.set_title('Department Distribution - Employee Count', fontsize=14, fontweight='bold', pad=20)
    ax1.set_xlabel('Department', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Number of Employees', fontsize=12, fontweight='bold')
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(axis='y', alpha=0.3)
    
    # Pie chart - Department Percentage
    explode = [0.1 if dept == 'IT' else 0 for dept in dept_counts.index]
    wedges, texts, autotexts = ax2.pie(dept_counts.values, labels=dept_counts.index, 
                                      autopct='%1.1f%%', startangle=90,
                                      colors=colors, explode=explode,
                                      shadow=True)
    
    ax2.set_title('Department Distribution - Percentage', fontsize=14, fontweight='bold', pad=20)
    
    # Make autotexts bold
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    plt.suptitle(f'Employee Department Analysis\nContact: 23f2004089@ds.study.iitm.ac.in', 
                fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    
    return fig, dept_counts

def save_as_html(df, fig, dept_counts):
    """Save analysis results and visualization as HTML."""
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Employee Department Analysis</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f5f5f5;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }}
            .header {{
                text-align: center;
                border-bottom: 3px solid #2E86AB;
                padding-bottom: 20px;
                margin-bottom: 30px;
            }}
            .analysis-section {{
                margin: 30px 0;
                padding: 20px;
                background-color: #f8f9fa;
                border-radius: 8px;
                border-left: 5px solid #2E86AB;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }}
            th, td {{
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #2E86AB;
                color: white;
            }}
            .it-highlight {{
                background-color: #e3f2fd;
                font-weight: bold;
            }}
            .contact {{
                text-align: center;
                margin-top: 40px;
                padding-top: 20px;
                border-top: 1px solid #ddd;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📊 Employee Department Analysis Report</h1>
                <p>Generated on {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            
            <div class="analysis-section">
                <h2>📈 Executive Summary</h2>
                <p>This analysis examines the distribution of employees across different departments, 
                with special focus on the IT department which is critical for organizational technology needs.</p>
            </div>
            
            <div class="analysis-section">
                <h2>🔢 IT Department Analysis</h2>
                <table>
                    <tr>
                        <th>Metric</th>
                        <th>Value</th>
                    </tr>
                    <tr class="it-highlight">
                        <td>IT Department Employee Count</td>
                        <td>{dept_counts.get('IT', 0)}</td>
                    </tr>
                    <tr>
                        <td>Total Employees</td>
                        <td>{len(df)}</td>
                    </tr>
                    <tr>
                        <td>IT Department Percentage</td>
                        <td>{(dept_counts.get('IT', 0) / len(df) * 100):.1f}%</td>
                    </tr>
                </table>
            </div>
            
            <div class="analysis-section">
                <h2>📋 Complete Department Distribution</h2>
                <table>
                    <tr>
                        <th>Department</th>
                        <th>Employee Count</th>
                        <th>Percentage</th>
                    </tr>
    """
    
    # Add department rows
    for dept, count in dept_counts.items():
        percentage = (count / len(df)) * 100
        row_class = 'it-highlight' if dept == 'IT' else ''
        html_content += f"""
                    <tr class="{row_class}">
                        <td>{dept}</td>
                        <td>{count}</td>
                        <td>{percentage:.1f}%</td>
                    </tr>
        """
    
    html_content += f"""
                </table>
            </div>
            
            <div class="analysis-section">
                <h2>📊 Visualization</h2>
                <p>The charts below visualize the department distribution:</p>
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{fig_to_base64(fig)}" alt="Department Distribution Charts" style="max-width: 100%; border-radius: 8px;">
                </div>
            </div>
            
            <div class="analysis-section">
                <h2>📝 Sample Data (First 10 Rows)</h2>
                {df.head(10).to_html(index=False, classes='dataframe')}
            </div>
            
            <div class="contact">
                <p><strong>Analysis performed by:</strong> 23f2004089@ds.study.iitm.ac.in</p>
                <p><strong>Report Type:</strong> Department Frequency Analysis</p>
                <p><strong>Dataset:</strong> Sample Employee Data ({len(df)} records)</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Save HTML file
    with open('employee_analysis.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("=" * 60)
    print("HTML REPORT GENERATED:")
    print("-" * 40)
    print("File saved as: employee_analysis.html")
    print("Open in web browser to view the complete analysis report.")

def fig_to_base64(fig):
    """Convert matplotlib figure to base64 string for HTML embedding."""
    from io import BytesIO
    import base64
    
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode('utf-8')
    return img_str

def main():
    """Main function to run the analysis."""
    
    print("Starting Employee Department Analysis...")
    print("=" * 60)
    
    # 1. Create sample employee data
    df = create_sample_data()
    print("✅ Sample employee data created successfully")
    print(f"   Total records: {len(df)}")
    
    # 2. Analyze department frequencies
    fig, dept_counts = analyze_departments(df)
    print("✅ Department analysis completed")
    
    # 3. Save as HTML file
    save_as_html(df, fig, dept_counts)
    print("✅ HTML report generated successfully")
    
    # 4. Save visualization separately as PNG
    fig.savefig('department_distribution.png', dpi=100, bbox_inches='tight')
    print("✅ Visualization saved as: department_distribution.png")
    
    print("=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    print("\nFiles created:")
    print("1. employee_analysis.html - Complete interactive report")
    print("2. department_distribution.png - Visualization chart")
    print("\nFor questions: 23f2004089@ds.study.iitm.ac.in")

if __name__ == "__main__":
    main()