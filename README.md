# House_price_prediction-app


## House Price Prediction App using Flask

### Overview

This Flask web application predicts the price of a house based on various features using a linear regression model. The model was trained on a dataset of house prices and features, and it has been deployed to this app for real-time predictions.

### Features

- Predicts house prices based on user-provided features
- Uses a linear regression model for prediction
- Provides a user-friendly interface for inputting features and getting predictions

### Requirements

- Python 3.6 or later
- Flask
- NumPy
- Pandas
- Scikit-learn

### Installation

1. Clone this repository: `git clone https://github.com/your-username/house-price-prediction-app.git`
2. Install the required dependencies: `pip install -r requirements.txt`

### Usage

1. Start the app: `flask run`
2. Go to `http://localhost:5000/` in your browser
3. Enter the house features in the form
4. Click the "Predict" button
5. The predicted house price will be displayed

### Model Comparison

We compared the performance of linear regression with other classification algorithms, including:

- Logistic Regression
- Decision Tree
- Random Forest

Linear regression outperformed the other algorithms in terms of accuracy and mean squared error.

### Disclaimer

The predictions made by this app are for informational purposes only and should not be relied upon for making financial decisions. The accuracy of the predictions may vary depending on the quality of the input data and the limitations of the linear regression model.
