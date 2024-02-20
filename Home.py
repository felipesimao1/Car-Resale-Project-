import streamlit as st

st.set_page_config(page_title="Car Resale Price Prediction App", page_icon="🚗", layout="wide")

def page_summary_body():

    st.title("Business Case and Dataset Summary")
    st.title("Welcome to our Car Resale Price Prediction App!")

    # Business Case Introduction
    st.info(
        f"**Business Case: Predicting Car Resale Prices**\n"
        f"John is a car salesman who owns a dealership specializing in used vehicles. "
        f"He wants to understand how car resale prices are determined to optimize his pricing strategy "
        f"and increase his dealership's profits. The challenge is to develop a predictive model that can "
        f"accurately estimate the resale prices of cars based on some factors such as year and price. "
    )

    # Objectives
    st.success(
        f"**Objectives:**\n"
        f"1. Build a machine learning model to predict resale prices for used cars.\n"
        f"2. Identify key factors influencing car resale prices.\n"
        f"3. Provide actionable insights to optimize pricing strategies and maximize profits."
    )

    # Approach
    st.warning(
        f"**Approach:**\n"
        f"- Collect a comprehensive dataset containing information about various cars.\n"
        f"- Train the chosen model and evaluate its performance using appropriate metrics.\n"
        f"- Analyze the model's predictions and identify influential factors affecting car resale prices."
    )

    # Expected Outcome
    st.info(
        f"**Expected Outcome:**\n"
        f"By developing a robust predictive model, the client expects to:\n"
        f"- Gain insights into pricing dynamics of the used car market.\n"
        f"- Improve dealership's pricing strategies based on accurate predictions.\n"
        f"- Enhance customer satisfaction by offering fair and competitive prices.\n"
        f"- Increase sales and profitability by optimizing inventory management and pricing decisions."
    )

    # Conclusion
    st.success(
        f"**Conclusion:**\n"
        f"By leveraging machine learning techniques, John can make data-driven decisions that enhance "
        f"competitiveness and profitability of his dealership. Understanding factors driving car prices "
        f"empowers him to stay ahead of the competition and better meet the needs of customers in the "
        f"dynamic automotive market."
    )

page_summary_body()
