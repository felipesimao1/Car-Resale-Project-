import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Título da página
    st.title("Car Price Prediction - Scatter Plots with Trend Lines")

    # Carregar os dados
    car_data = pd.read_csv('data/car_data.csv')

    # Definir as colunas e os títulos para os gráficos de dispersão
    scatter_plots = [
        {'x_column': 'Year', 'y_column': 'Selling_Price', 'title': 'Year vs Selling Price',
         'text': "Our scatter plot 'Year vs Selling Price' reveals an interesting trend: newer cars tend to have higher selling prices. This positive correlation between the car's year and selling price suggests that customers value novelty and technology when making a purchase decision."},
        
        {'x_column': 'Kms_Driven', 'y_column': 'Selling_Price', 'title': 'Kms Driven vs Selling Price',
         'text': "In our scatter plot 'Kms Driven vs Selling Price,' we observe a more complex trend. While cars with fewer kilometers driven tend to have higher selling prices, there is significant dispersion in the data, indicating that other factors also play an important role in determining the selling price."},
        
        {'x_column': 'Present_Price', 'y_column': 'Selling_Price', 'title': 'Present Price vs Selling Price',
         'text': "Lastly, the scatter plot 'Present Price vs Selling Price' allows us to assess how the current market price influences the selling price. We observe a strong positive correlation between these two variables, suggesting that customers are willing to pay more for cars with higher market prices. This underscores the importance of considering the current value of the car when determining its selling price."}
    ]

    # Criar e exibir os gráficos de dispersão com linha de tendência
    for plot in scatter_plots:
        st.header(plot['title'])
        st.write(plot['text'])
        fig, ax = plt.subplots()
        sns.regplot(x=plot['x_column'], y=plot['y_column'], data=car_data, scatter=True, ci=None, ax=ax)
        ax.set_xlabel(plot['x_column'])
        ax.set_ylabel(plot['y_column'])
        ax.set_title('Scatter Plot with Trend Line: ' + plot['title'])
        st.pyplot(fig)

if __name__ == "__main__":
    main()
