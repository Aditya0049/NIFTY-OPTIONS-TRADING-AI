import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def generate_trade_recommendations():
    # Load the historical data from the CSV file.
    df = pd.read_csv("data/historical_data.csv")

    # Create the linear regression model.
    lr = LinearRegression()
    lr.fit(df[["Open", "High", "Low", "Close"]], df["Volume"])

    # Calculate the predicted movement of the Nifty index.
    predicted_movement = lr.predict(df[["Open", "High", "Low", "Close"]])

    # Identify the days when the Nifty index is expected to make less than 1% of movement.
    low_movement_days = df[predicted_movement < 0.01]

    # Generate trade recommendations for the days with low movement.
    trade_recommendations = []
    for date, open_price, high_price, low_price, close_price in low_movement_days.itertuples():
        # Sell ATM+1% call options.
        trade_recommendations.append({
            "date": date,
            "recommendation": "Sell ATM+1% call options"
        })
        # Sell ATM+1% put options.
        trade_recommendations.append({
            "date": date,
            "recommendation": "Sell ATM+1% put options"
        })

    return trade_recommendations

@app.route('/')
def index():
    trade_recommendations = generate_trade_recommendations()
    return render_template('index.html', trade_recommendations=trade_recommendations)

if __name__ == '__main__':
    app.run(debug=True)