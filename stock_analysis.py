import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv('stock_index.csv')

# Create a new column called "predicted_direction"
data['predicted_direction'] = np.where(data['close'] > data['open'], 1, -1)

# Split the data into training and test sets
train_data = data[data['date'] < '2023-01-01']
test_data = data[data['date'] >= '2023-01-01']

# Create the model
model = LinearRegression()

# Train the model
model.fit(train_data['open'], train_data['close'])

# Make predictions on the test set
predictions = model.predict(test_data['open'])

# Evaluate the model
print('Accuracy:', model.score(test_data['open'], test_data['close']))
