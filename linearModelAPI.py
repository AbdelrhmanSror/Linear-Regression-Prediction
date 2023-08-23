from fastapi import FastAPI, Query, HTTPException
from fastapi.testclient import TestClient
from sklearn.linear_model import LinearRegression

import numpy as np
import pandas as pd

app = FastAPI()

# Load the CSV data into a pandas DataFrame
data = pd.read_csv("F:\probelm_solving\henkel/example.csv")

# Extract features (X) and target (Y)
x = data[["X0", "X1", "X2"]]
y = data["Y"]

# Train a linear regression model
model = LinearRegression()
model.fit(x, y)


@app.get("/predict")
def read_independents(x0: float = Query(...), x1: float = Query(...), x2: float = Query(...)):
    """
    Predict the target variable (Y) using the trained linear regression model.

    Parameters:
    - x0: Feature value for X0
    - x1: Feature value for X1
    - x2: Feature value for X2

    Returns:
    - Predicted y value
    """
    try:
        input_data = np.array([[x0, x1, x2]])
        predicted_y = model.predict(input_data)[0]
        return {
            "message": "Predicted y value",
            "input_x0": x0,
            "input_x1": x1,
            "input_x2": x2,
            "predicted_y": predicted_y
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/equation")
def get_equation():
    """
    Get the equation of the trained linear regression model.

    Returns:
    - Equation of the form: y = intercept + coefficient_X0 * X0 + coefficient_X1 * X1 + coefficient_X2 * X2
    """
    coefficients = model.coef_
    intercept = model.intercept_
    equation = "y = {} + {} X0 + {} X1 + {} X2".format(
        round(intercept, 2), round(coefficients[0], 2),
        round(coefficients[1], 2), round(coefficients[2], 2)
    )
    return {"equation": equation}

# Test cases for the endpoints


def test_predict_endpoint():
    client = TestClient(app)
    response = client.get("/predict?x0=300&x1=200&x2=50")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert "predicted_y" in data


def test_equation_endpoint():
    client = TestClient(app)
    response = client.get("/equation")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert "equation" in data


if __name__ == "__main__":
    test_predict_endpoint()
    test_equation_endpoint()
