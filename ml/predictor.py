import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load the trained model
def predict():
    with open("./train/xgb_model.pkl", "rb") as f:
        xgb_model = pickle.load(f)
    # Read new data from Excel file
    df_new_data = pd.read_excel(f"./ml/readyxl.xlsx")
    # Make predictions using the loaded model
    predictions = xgb_model.predict(df_new_data)
    return predictions

