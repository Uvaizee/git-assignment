import pandas as pd
import numpy as np

# Sample dataset
data = {
    'age': [25, 30, 45, 35, 50],
    'salary': [50000, 60000, 80000, 65000, 120000]
}
df = pd.DataFrame(data)

# Function to add new features
def add_features(df):
    # Adding a numerical feature: Logarithm of salary
    df['log_salary'] = np.log(df['salary'])
    
    # Adding a binary feature: Age category (1 if age > 30, else 0)
    df['age_above_30'] = df['age'].apply(lambda x: 1 if x > 30 else 0)
    
    # Adding a categorical feature: Age group
    df['age_group'] = pd.cut(df['age'], bins=[0, 25, 35, 50, 100], labels=['Young', 'Adult', 'Middle-aged', 'Senior'])
    
    return df

# Add the features and display the updated DataFrame
df = add_features(df)
print(df)
