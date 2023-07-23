import numpy as np

class LinearRegression:

    def __init__(self):
        self.coefficients = None
        self.intercept = None

    def fit(self, x_data, y_data):
        """
        Fits the linear regression model to the data.

        Args:
            x_data: The independent variables.
            y_data: The dependent variables.

        Returns:
            None.
        """

        # Create a NumPy array for the x-data.
        x_array = np.array(x_data)

        # Create a NumPy array for the y-data.
        y_array = np.array(y_data)

        # Calculate the coefficients of the linear regression model.
        self.coefficients = np.linalg.lstsq(x_array, y_array, rcond=-1)[0]

        # Calculate the intercept of the linear regression model.
        self.intercept = np.mean(y_data) - np.dot(self.coefficients, np.mean(x_data))

    def predict(self, x_data):
        """
        Makes predictions for the given data.

        Args:
            x_data: The data to make predictions for.

        Returns:
            A NumPy array of predictions.
        """

        # Create a NumPy array for the x-data.
        x_array = np.array(x_data)

        # Make predictions for the given data.
        predictions = np.dot(x_array, self.coefficients) + self.intercept

        return predictions
