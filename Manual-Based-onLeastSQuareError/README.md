# Linear Regression FastAPI Application

This is a FastAPI application that performs linear regression and prediction on a given set of features (X0, X1, X2) to predict the target variable (Y).

## Description

This FastAPI application demonstrates how to perform linear regression using the provided CSV dataset and make predictions using the trained model. The model is trained using the least squares method to fit a linear equation to the data.

The core functionality of the application lies in predicting the target variable using linear regression. There are two versions of the implementation showcased here:

1. This code snippet performs linear regression manually by calculating the coefficients and intercept using numpy operations. This approach provides an understanding of the underlying calculations involved in linear regression.
2. while The code snippet, available in the [provided GitHub repository](https://github.com/AbdelrhmanSror/Linear-Regression-Prediction), utilizes the scikit-learn library to train a linear regression model. This method offers a more concise and standard way of implementing the linear regression task.

## Installation

1. Clone the repository to your local machine.
2. Make sure you have Python installed (version 3.6 or higher).
3. Install the required packages using the following command:

   ```bash
   pip install fastapi pandas numpy scikit-learn
   ```

## Usage

1. Place your CSV dataset in the root directory with the filename `example.csv`.
2. Choose the implementation you wish to use:
   - If you want to explore manual calculations, use this code snippet.
   - If you prefer a more streamlined approach, refer to the code snippet from the [GitHub repository](https://github.com/AbdelrhmanSror/Linear-Regression-Prediction).
3. Run the FastAPI application using the following command:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

4. Access the Swagger documentation and interact with the endpoints:
   - `/predict`: Predict the target variable (Y) based on provided feature values (X0, X1, X2).
   - `/equation`: Retrieve the equation of the linear regression model.

## Endpoints

### Predict Endpoint

Predict the target variable (Y) using the trained linear regression model.

**URL:** `/predict`

**Method:** GET

**Parameters:**
- `x0`: Feature value for X0
- `x1`: Feature value for X1
- `x2`: Feature value for X2

**Response:**
```json
{
    "message": "Predicted y value",
    "input_x0": x0,
    "input_x1": x1,
    "input_x2": x2,
    "predicted_y": predicted_y
}
```

### Equation Endpoint

Get the equation of the linear regression model.

**URL:** `/equation`

**Method:** GET

**Response:**
```json
{
    "equation": "y = a + b0 * x0 + b1 * x1 + b2 * x2"
}
```

## Test Cases

This application includes test cases for the endpoints. To run the tests:

1. Ensure the FastAPI application is running.
2. Execute the test cases script:

   ```bash
   python test_cases.py
   ```

## Additional Implementation

If you're interested in an alternative implementation of the linear regression task using scikit-learn, refer to the [GitHub repository](https://github.com/AbdelrhmanSror/Linear-Regression-Prediction). The provided code offers a concise and standard approach to linear regression, utilizing scikit-learn's built-in functionalities.

---

Feel free to explore both implementations and choose the one that best suits your needs. If you have any questions or encounter any issues, don't hesitate to reach out to the project contributors.

---
