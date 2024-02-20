import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def load_data():
    # Carregar os dados do arquivo CSV
    df = pd.read_csv('data/car_data.csv')

    # Codificar as colunas categóricas
    df.replace({'Fuel_Type': {'Petrol': 0, 'Diesel': 1, 'CNG': 2},
                'Seller_Type': {'Dealer': 0, 'Individual': 1},
                'Transmission': {'Manual': 0, 'Automatic': 1}}, inplace=True)

    return df

def train_model(df):
    # Definir X e Y
    X = df.drop(['Car_Name', 'Selling_Price'], axis=1)
    y = df['Selling_Price']

    # Dividir os dados em conjunto de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=2)

    # Carregar o modelo de regressão linear
    lin_reg_model = LinearRegression()

    # Treinar o modelo
    lin_reg_model.fit(X_train, y_train)

    # Fazer previsões no conjunto de treinamento
    training_data_prediction = lin_reg_model.predict(X_train)

    # Calcular o erro R ao quadrado
    error_score = metrics.r2_score(y_train, training_data_prediction)

    return lin_reg_model, error_score

def main():
    st.title("Car Price Prediction App")

    # Carregar os dados
    df = load_data()

    # Treinar o modelo
    model, error_score = train_model(df)

    # Exibir informações sobre o modelo
    st.header("Model Information")
    st.write("This section provides information about the trained linear regression model.")
    st.write("Coefficient: ", model.coef_)
    st.write("Intercept: ", model.intercept_)
    st.write("R-squared Error: ", error_score)

    # Exibir informações sobre os dados
    st.header("Data Information")
    st.write("This section provides information about the dataset used for training the model.")
    st.write("Dataset Shape: ", df.shape)
    st.write("First 5 Rows of Data:")
    st.write(df.head())

    # Gráfico de dispersão entre preço de venda real e preço de venda previsto
    st.header("Scatter Plot for Actual vs Predicted Selling Price")
    st.write("This scatter plot compares the actual selling price of cars with the price predicted by the linear regression model.")
    st.write("Using Test Data")
    X_test = df.drop(['Car_Name', 'Selling_Price'], axis=1)
    y_test = df['Selling_Price']
    y_pred = model.predict(X_test)
    scatter_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    st.write(scatter_df.head())
    st.write("Scatter Plot:")
    st.write("Each point on the plot represents a car from the dataset. The x-axis represents the actual selling price, while the y-axis represents the predicted selling price by the model.")
    st.line_chart(scatter_df)


if __name__ == "__main__":
    main()
