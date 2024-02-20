import streamlit as st
import pandas as pd

def main():
    # Read the first few lines of the car_data.csv file
    df = pd.read_csv('data/car_data.csv')
    first_lines = df.head()

    # Display the first few lines on the page
    st.write(
             f"First Lines of the car_data.csv File:\n"
             f"We can see the first few lines of the car_data.csv file below:\n"
             f"We have 9 colums in the dataset:\n"
             f"Car_Name, Year, Selling_Price, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, and Owner.\n")

    st.write(first_lines)

    # Extract two columns
    two_columns = df[['Year', 'Car_Name']].head()

    # Display the first few lines on the page
    st.write("First Lines of the 'Year' and 'Car_Name' Columns from the car_data.csv File:")
    st.write(two_columns)

    # Read the content of the car_info.txt file
    with open('notebooks/car_info.txt', 'r') as file:
        content = file.read()

    # Display the information in a table
    st.title("Dataset.info() Method Output for the Car Dataset")
    st.write("Here are the dataset details:")
    st.text(content)

    # Read the content of the car_dataset_encoded.txt file
    with open('notebooks/car_dataset_encoded.txt', 'r') as file:
        content2 = file.read()

    # Display the information in a table
    st.title("Preprocessed Car Dataset. Here we just encoded the categorical columns. ")
    st.write("Here are the dataset details:")
    st.text(content2)

if __name__ == "__main__":
    main()
