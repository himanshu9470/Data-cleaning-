import pandas as pd
import matplotlib.pyplot as plt

def clean_and_visualize(input_file, output_file):

    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file, na_values=['', ' ', 'nan', 'NaN', 'NA', 'N/A'])
    else:
        df = pd.read_excel(input_file, na_values=['', ' ', 'nan', 'NaN', 'NA', 'N/A'])
    
    original_shape = df.shape
    print(f"Original data shape: {original_shape}")
    print(f"Initial missing values:\n{df.isna().sum()}")
    
    # Create visualization figure
    plt.figure(figsize=(18, 12))
    plt.suptitle('Data Cleaning Process Visualization', fontsize=16)
    
    # 1. Missing values before cleaning
    plt.subplot(3, 3, 1)
    df.isna().sum().sort_values().plot(kind='barh')
    plt.title('Missing Values Before Cleaning')
    plt.xlabel('Count')
    
    # 2. Data cleaning steps
    cols_before = set(df.columns)
    df = df.dropna(axis=1, thresh=len(df)*0.1)
    cols_after = set(df.columns)
    dropped_cols = cols_before - cols_after
    if dropped_cols:
        print(f"\nDropped columns with >90% missing values: {dropped_cols}")
    
    # Convert empty strings to NaN and standardize categorical values
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    for col in categorical_cols:
        df[col] = df[col].astype(str).str.strip().replace({'nan': pd.NA})
        if col in ['Sex', 'Embarked']: 
            df[col] = df[col].str.upper()
    for col in df.columns:
        if df[col].isna().sum() > 0:
            if pd.api.types.is_numeric_dtype(df[col]):
                fill_val = df[col].median()
                df[col].fillna(fill_val, inplace=True)
                print(f"Filled {col} (numeric) with median: {fill_val:.2f}")
            else:
                df[col].fillna('UNKNOWN', inplace=True)
                print(f"Filled {col} (categorical) with 'UNKNOWN'")
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()
    cleaned_shape = df.shape
    print(f"\nRemoved {duplicates} duplicate rows")
    
    # 3. Missing values after cleaning
    plt.subplot(3, 3, 2)
    df.isna().sum().sort_values().plot(kind='barh', color='green')
    plt.title('Missing Values After Cleaning')
    plt.xlabel('Count')
    
    # 4. Data volume comparison
    plt.subplot(3, 3, 3)
    plt.barh(['Original', 'Cleaned'], 
            [original_shape[0], cleaned_shape[0]],
            color=['blue', 'green'])
    plt.title('Row Count Comparison')
    plt.xlabel('Number of Rows')
    
    # 5. Column count comparison
    plt.subplot(3, 3, 4)
    plt.barh(['Original', 'Cleaned'], 
            [original_shape[1], cleaned_shape[1]],
            color=['red', 'orange'])
    plt.title('Column Count Comparison')
    plt.xlabel('Number of Columns')
    
    # 6. numeric column distribution (Age)
    if 'Age' in df.columns:
        plt.subplot(3, 3, 5)
        plt.hist(df['Age'], bins=20, color='purple', edgecolor='black')
        plt.title('Age Distribution After Cleaning')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
    
    # 7. categorical column distribution (Sex)
    if 'Sex' in df.columns:
        plt.subplot(3, 3, 6)
        df['Sex'].value_counts().plot(kind='bar', color='teal')
        plt.title('Passenger Gender Distribution')
        plt.ylabel('Count')
    
    # 8. Survival rate by class
    if all(col in df.columns for col in ['Survived', 'Pclass']):
        plt.subplot(3, 3, 7)
        pd.crosstab(df['Pclass'], df['Survived'], normalize='index').plot(
            kind='bar', stacked=True, color=['red', 'green'])
        plt.title('Survival Rate by Passenger Class')
        plt.ylabel('Proportion')
        plt.legend(['Died', 'Survived'], bbox_to_anchor=(1, 1))
    
    # 9. Fare distribution
    if 'Fare' in df.columns:
        plt.subplot(3, 3, 8)
        plt.boxplot(df['Fare'], vert=False)
        plt.title('Fare Distribution')
        plt.xlabel('Fare')
    
    plt.tight_layout()
    
    if output_file.endswith('.csv'):
        df.to_csv(output_file, index=False)
    else:
        df.to_excel(output_file, index=False)
    
    # Show summary statistics
    print("\n=== Summary Statistics ===")
    print(df.describe(include='all'))
    
    plt.show()
    
    print(f"\nCleaning complete! Data saved to {output_file}")
    print(f"Original shape: {original_shape}")
    print(f"Cleaned shape: {cleaned_shape}")

if __name__ == "__main__":
    input_file = "realistic_titanic_sample.csv"  # input file
    output_file = "cleaned_titanic_data.csv"     # Output file
    
    clean_and_visualize(input_file, output_file)
