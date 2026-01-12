import pandas as pd

# Load training data
train_df = pd.read_csv("data/UNSW_NB15_training-set.csv")

# Drop non-numeric / irrelevant columns
drop_cols = ['id', 'attack_cat', 'label']
X_train = train_df.drop(columns=drop_cols, errors='ignore')

# Keep only numeric features
X_train = X_train.select_dtypes(include=['int64', 'float64'])

# Train ONLY on normal traffic
X_train_normal = X_train[train_df['label'] == 0]

# Handle missing values
X_train_normal.fillna(0, inplace=True)

# Save processed data
X_train_normal.to_csv("data/train_normal.csv", index=False)

print("Preprocessing complete. Normal traffic saved.")
