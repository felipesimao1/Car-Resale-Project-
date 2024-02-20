
import streamlit as st

def main():
    st.title("Welcome to our Car Resale Price Prediction App!")

    st.write("""
    **Project Objective:**

    Our objective is to develop a Machine Learning model capable of predicting the resale price of cars based on various features.

    **Business Case:**

    The resale price of a car is influenced by various factors such as its make, model, year of manufacture, mileage, fuel type, seller type, transmission type, and ownership history. Predicting the resale price accurately can assist both sellers and buyers in making informed decisions.

    **How Our App Works:**

    1. **Data Exploration and Preprocessing:** We start by exploring the dataset containing information about car features and their resale prices. This includes understanding the distribution of features, identifying missing data, and exploring correlations between features and the resale price. We also preprocess the data by handling missing values, encoding categorical variables, and splitting the dataset into training and testing sets.


    2. **Model Training and Evaluation:** We select and train a suitable regression model, such as Linear Regression, Decision Tree Regression, or Random Forest Regression, using the training data. In this project we have used Linear Regression model. We evalue the performance of the trained model using metrics like Interception and R-squared Error to assess how well it predicts resale prices.

    3. **Model Learning Curves:** We visualize the learning curve of our machine learning model to understand how its performance changes as we vary the size of the training dataset. This helps us understand how the model learns from additional data.
             
    4. **Scatter Plots with Trend Lines:** We create scatter plots with trend lines to visualize the relationships between car features and their resale prices. This allows us to identify trends and patterns that can help us understand how different features influence the resale price of cars.

    **Why Use Our App:**

    - **Accurate Predictions:** Our model is trained on a comprehensive dataset, ensuring accurate predictions of car resale prices.
    - **User-Friendly Interface:** Our app provides a simple and intuitive interface, making it easy for users to input car features and obtain predictions quickly.
    - **Informed Decision-Making:** Whether you're a seller looking to set a competitive price or a buyer aiming to make a smart purchase, our app provides valuable insights to aid your decision-making process.

    **Get Started:** Try out our Car Resale Price Prediction App now and make informed decisions when buying or selling your next car!
    """)

if __name__ == "__main__":
    main()