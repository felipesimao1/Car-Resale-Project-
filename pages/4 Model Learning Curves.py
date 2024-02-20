import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve, train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def load_data():
    df = pd.read_csv('data/car_data.csv')

    # Codificar as colunas categóricas
    df.replace({'Fuel_Type': {'Petrol': 0, 'Diesel': 1, 'CNG': 2},
                'Seller_Type': {'Dealer': 0, 'Individual': 1},
                'Transmission': {'Manual': 0, 'Automatic': 1}}, inplace=True)

    return df

def train_model(df):
    X = df.drop(['Car_Name', 'Selling_Price'], axis=1)
    y = df['Selling_Price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=2)
    lin_reg_model = LinearRegression()
    train_sizes, train_scores, test_scores = learning_curve(lin_reg_model, X_train, y_train, cv=5)
    return train_sizes, train_scores, test_scores, X_test, y_test

def plot_learning_curve(train_sizes, train_scores, test_scores):
    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, np.mean(train_scores, axis=1), label='Training score')
    plt.plot(train_sizes, np.mean(test_scores, axis=1), label='Cross-validation score')
    plt.title('Learning Curves')
    plt.xlabel('Training Size')
    plt.ylabel('Score')
    plt.legend()
    return plt.gcf()  # Return the current figure

def main():
    st.title("Car Price Prediction App")

    df = load_data()
    train_sizes, train_scores, test_scores, X_test, y_test = train_model(df)

    st.title("Model Learning Curves")
    st.header("Learning Curves")
    st.write("Our learning curve graph provides valuable insights into how our machine learning model performs as we vary the size of the training dataset. The x-axis represents the training size, indicating the number of data points used for training, while the y-axis represents the model's performance score, which can measure accuracy or error.\n\nAs we increase the training size, we can observe changes in the model's performance, helping us understand how the model learns from additional data.")

    fig = plot_learning_curve(train_sizes, train_scores, test_scores)
    st.pyplot(fig)  # Pass the figure object to st.pyplot()

if __name__ == "__main__":
    main()
