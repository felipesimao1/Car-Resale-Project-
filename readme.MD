
# Car Price Prediction App

This Streamlit web application is designed to predict the resale price of cars based on various features. It utilizes a linear regression machine learning model trained on a dataset containing information about different car models and their respective selling prices.

## Features

- **Input Features**: Users can input various features of a car, such as its year of manufacture, fuel type, seller type, transmission type, etc.
- **Prediction**: After providing the necessary input features, the app predicts the selling price of the car based on the trained machine learning model.
- **Visualization**: The app also provides visualizations such as scatter plots to compare actual selling prices with predicted selling prices.

## Dataset

The dataset used for training the machine learning model can be found on Kaggle: [Car Resale Price Dataset](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho?resource=download).

## Requirements

To run this application locally, you need the following dependencies:

- Python 3.x
- Streamlit
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```
## Usage

To launch the application, navigate to the project directory and run the following command:
```bash
streamlit run app.py
```
