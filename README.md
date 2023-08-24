# Linear-Regression-Prediction
This repository contains a FastAPI-based API that implements a simple linear regression model for predicting a target variable based on input features.

## Description

This FastAPI application loads a CSV dataset containing feature (X) and target (Y) values. It then trains a linear regression model using scikit-learn and provides two endpoints:

1. **/predict**: Accepts input feature values and returns a prediction for the target variable using the trained model.
2. **/equation**: Returns the equation of the trained linear regression model.

## Dependencies

Make sure you have the following dependencies installed before running the code:

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast, web framework for building APIs with Python 3.7+.
- [uvicorn](https://www.uvicorn.org/): ASGI server implementation to run the FastAPI application.
- [scikit-learn](https://scikit-learn.org/stable/): Machine learning library for Python.
- [numpy](https://numpy.org/): Fundamental package for scientific computing in Python.
- [pandas](https://pandas.pydata.org/): Data manipulation and analysis library.
- [httpx](https://www.python-httpx.org/): Asynchronous HTTP client for Python, important for emulating tests with the TestClient.

You can install these dependencies using the following command:

```bash
pip install fastapi uvicorn scikit-learn numpy pandas httpx
```

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/AbdelrhmanSror/Linear-Regression-Prediction.git
```

2. Navigate to the project directory:

```bash
cd Linear-Regression-Prediction
```

3. Run the FastAPI application using uvicorn:

```bash
uvicorn linearModelAPI:app --reload
```

4. Once the server is running, you can access the endpoints in your browser or using tools like `curl` or Postman.

- Prediction Endpoint: http://127.0.0.1:8000/predict?x0=300&x1=200&x2=50
- Equation Endpoint: http://127.0.0.1:8000/equation

## Testing

The repository includes test cases to ensure the functionality of the endpoints. To run the tests, execute the following command:

```bash
python linearModelAPI.py
```
