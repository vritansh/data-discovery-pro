import matplotlib.pyplot as plt
import pandas as pd
from ddpro._readconfig import *


__all__ =['Visualize']

class Visualize():

    def __init__(self):
        self.config = config

    def bar_plot_from_dict(self, data_dict, label='VISUALIZATION_BAR_PLOT_DEFAULT'):
        """
         Bar plot from the dictinoary. Second argument is for labeling
        :param data:
        :param label:
        :return:
        """
        if(len(data_dict)==0):
           return

        x = list(data_dict.keys())
        y = list(data_dict.values())
        plt.bar(x, y, align='center',tick_label=x)
        print(list(x))

        plt.ylabel(self.config.get(label, 'Y_LABEL'))
        plt.xlabel(self.config.get(label, 'X_LABEL'))
        plt.title(self.config.get(label, 'TITLE'))
        plt.xticks(rotation=self.config.get(label, 'ROTATION'))

        plt.show()

