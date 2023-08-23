from fastapi import FastAPI, Query, HTTPException
import numpy as np
import pandas as pd
from fastapi.testclient import TestClient

app = FastAPI()

# Load the CSV data into a pandas DataFrame
data = pd.read_csv("F:\probelm_solving\henkel/example.csv")
means = np.mean(data, axis=0)
mean_x0, mean_x1, mean_x2, mean_y = means[1:]

# Line equation is: y = a + b0 * x0 + b1 * x1 + b2 * x2


def slope(x, y, mean_x, mean_y):
    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator = np.sum((x - mean_x) ** 2)
    b = numerator / denominator
    return b


b0 = slope(data["X0"], data["Y"], mean_x0, mean_y)
b1 = slope(data["X1"], data["Y"], mean_x1, mean_y)
b2 = slope(data["X2"], data["Y"], mean_x2, mean_y)
a = mean_y - b0 * mean_x0 - b1 * mean_x1 - b2 * mean_x2

equation = "y = {} + {} X0 + {} X1 + {} X2".format(
    round(a), round(b0), round(b1), round(b2))


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
        predicted_y = a + b0 * x0 + b1 * x1 + b2 * x2
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
    Get the equation of the linear regression model.

    Returns:
    - Equation of the form: y = a + b0 * x0 + b1 * x1 + b2 * x2
    """
    return {"equation": equation}


# Test cases for the endpoints
client = TestClient(app)


def test_predict_endpoint():
    response = client.get("/predict?x0=300&x1=200&x2=50")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert "predicted_y" in data


def test_equation_endpoint():
    response = client.get("/equation")
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert "equation" in data

# Run the test cases


if __name__ == "__main__":
    test_predict_endpoint()
    test_equation_endpoint()
