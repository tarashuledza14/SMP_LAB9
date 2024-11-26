import matplotlib.pyplot as plt
from Lab_8.BasicVisualizer import BasicVisualizer


class AdvancedVisualizer(BasicVisualizer):
    def plot_scatter(self, x_column, y_column):
        plt.figure(figsize=(8, 6))
        plt.scatter(self.data[x_column], self.data[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"{y_column} vs {x_column}")
        plt.show()

    def plot_bar_chart(self, category_column, value_column):
        data_grouped = self.data.groupby(category_column)[value_column].mean()
        data_grouped.plot(kind='bar', figsize=(10, 5))
        plt.xlabel(category_column)
        plt.ylabel(f"Average {value_column}")
        plt.title(f"Average {value_column} by {category_column}")
        plt.show()
