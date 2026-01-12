import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load training data
train_df = pd.read_csv("data/UNSW_NB15_training-set.csv")

# Drop non-feature columns
drop_cols = ['id', 'attack_cat', 'label']
X = train_df.drop(columns=drop_cols, errors='ignore')

# Keep only numeric features
X = X.select_dtypes(include=['int64', 'float64'])
X.fillna(0, inplace=True)

# Train only on NORMAL traffic
X_normal = X[train_df['label'] == 0]

# Save feature names (CRITICAL)
joblib.dump(X_normal.columns.tolist(), "feature_names.pkl")

# Train model
model = IsolationForest(
    n_estimators=200,
    contamination=0.1,
    random_state=42
)

model.fit(X_normal)

# Save model
joblib.dump(model, "anomaly_model.pkl")

print("Model trained with features:", len(X_normal.columns))
