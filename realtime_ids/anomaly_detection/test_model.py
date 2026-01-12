import pandas as pd
import joblib

# Load model
model = joblib.load("anomaly_model.pkl")

# Load test data
test_df = pd.read_csv("data/UNSW_NB15_testing-set.csv")

# Prepare features
drop_cols = ['id', 'attack_cat', 'label']
X_test = test_df.drop(columns=drop_cols, errors='ignore')
X_test = X_test.select_dtypes(include=['int64', 'float64'])
X_test.fillna(0, inplace=True)

# Predict
predictions = model.predict(X_test)

# Convert prediction labels
#  1 = Normal, -1 = Anomaly
test_df['prediction'] = predictions
test_df['prediction'] = test_df['prediction'].map({
    1: 'Normal',
    -1: 'Anomaly'
})

# Save results
test_df.to_csv("data/anomaly_results.csv", index=False)

print(test_df['prediction'].value_counts())
