import matplotlib.pyplot as plt
from Lab_8.BasicVisualizer import BasicVisualizer


class MultiPlotVisualizer(BasicVisualizer):
    def plot_multiple(self):
        fig, axs = plt.subplots(1, 2, figsize=(12, 5))
        average_price_per_year = self.data.groupby('Year_of_Manufacture__c')['Sale_Price__c'].mean()
        axs[0].plot(average_price_per_year.index, average_price_per_year.values, marker='o', linestyle='-')
        axs[0].set_title('Sale Price Over Year')
        
        axs[1].scatter(self.data['Mileage__c'], self.data['Sale_Price__c'])
        axs[1].set_title('Milage vs Sale Price')
        
        plt.tight_layout()
        plt.show()
