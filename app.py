import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load the trained model
with open("./train/xgb_model.pkl", "rb") as f:
    xgb_model = pickle.load(f)

# Read new data from Excel file
df_new_data = pd.read_excel("./readyxl.xlsx")
# Make predictions using the loaded model
predictions = xgb_model.predict(df_new_data)

# Plotting the predictions
plt.figure(figsize=(10, 6))
plt.plot(predictions, label='Predicted Values', color='blue')
plt.xlabel('Data Points')
plt.ylabel('Predicted Productivity')
plt.title('Predicted Productivity vs. Data Points')
plt.legend()
plt.grid(True)
plt.show()
