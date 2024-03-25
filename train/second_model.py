import pandas as pd
import pickle
import xgboost as xgb

# Read training dataset from Excel file
df_train = pd.read_excel("./train_dataset.xlsx")
df_train["wip"] = df_train["wip"].fillna(df_train["wip"].mean())

# Define features and target variable for training
X_train = df_train.iloc[:, :-1]
y_train = df_train["actual_productivity"]

# Train XGBoost model
xgb_r = xgb.XGBRegressor(objective='reg:linear', n_estimators=10, seed=123)
xgb_r.fit(X_train, y_train)

# Save the trained model
with open("xgb_model.pkl", "wb") as f:
    pickle.dump(xgb_r, f)

# Now the trained model is saved as "xgb_model.pkl"
