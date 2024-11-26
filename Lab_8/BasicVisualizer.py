import matplotlib.pyplot as plt
import pandas as pd


class BasicVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_line_chart(self, x_column, y_column):
        average_price_per_year = self.data.groupby('Year_of_Manufacture__c')['Sale_Price__c'].mean()

        # Побудова лінійного графіка
        plt.figure(figsize=(10, 6))
        plt.plot(average_price_per_year.index, average_price_per_year.values, marker='o', color='g', linestyle='-')
        #plt.title("Середня ціна автомобілів за роками виробництва")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid(True)
        plt.show()