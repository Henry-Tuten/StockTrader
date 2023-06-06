# SET UP
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from trading_functions import place_buy_order, place_sell_order
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the master dataset
master_data = pd.read_csv('master_data.csv')

# Split the master data into features (X) and target variable (y)
X_master = master_data[['Feature1', 'Feature2', 'Feature3']]  # Replace with your actual feature columns
y_master = master_data['Target']  # Replace with your actual target column

# Create a linear regression model
model = LinearRegression()

# Train the model on the master dataset
model.fit(X_master, y_master)

# Function to update the model with new data and make predictions
def update_and_predict(new_data):
    # Append the new data to the master dataset
    updated_data = pd.concat([master_data, new_data])

    # Split the updated data into features (X) and target variable (y)
    X_updated = updated_data[['Feature1', 'Feature2', 'Feature3']]  # Replace with your actual feature columns
    y_updated = updated_data['Target']  # Replace with your actual target column

    # Retrain the model with the updated data
    model.fit(X_updated, y_updated)

    # Make predictions on the new data
    new_predictions = model.predict(new_data[['Feature1', 'Feature2', 'Feature3']])  # Replace with your actual feature columns

    return new_predictions

# Example usage:
# Load new data (in the same format as the master dataset)
new_data = pd.read_csv('new_data.csv')

# Make predictions on the new data
predictions = update_and_predict(new_data)

# Display the predictions
print("Predictions:", predictions)