import logging

import matplotlib.pyplot as plt
import pandas as pd
from ddpro._readconfig import *
import plotly.express as px


__all__ = ['Visualize']


class Visualize():
    """
    This class contains details of all the methods responsible for doing visualization. A plotly based visualization can be done by passing the flag.
    """

    def __init__(self):
        """
        Basic structre of the class is configuration object, matplotlib plt and px object
        """
        self.px = px
        self.plt = plt

    def bar_plot_from_dict(self, data_dict, label='VISUALIZATION_BAR_PLOT_DEFAULT'):
        """
         Bar plot from the dictinoary. Second argument is for labeling
        :param data:
        :param label:
        :return:
        """
        if (len(data_dict) == 0):
            return

        x = list(data_dict.keys())
        y = list(data_dict.values())
        plt.bar(x, y, align='center', tick_label=x)
        print(list(x))

        plt.ylabel(config.get(label, 'Y_LABEL'))
        plt.xlabel(config.get(label, 'X_LABEL'))
        plt.title(config.get(label, 'TITLE'))
        plt.xticks(rotation=config.get(label, 'ROTATION'))

        plt.show()

    def histogram_plot_from_dataframe(self, dataframe, columns, label='VISUALIZATION_HISTOGRAM_DEFAULT'):
        """
        This method plots a histogram for best describing the distribution of the data. It is run after cleaning the dataset
        :param data_dict:
        :param label:
        :return:
        """
        if (len(dataframe) == 0):
            return
        for c in columns:
            plt.hist(dataframe[c])

            plt.ylabel(config.get(label, 'Y_LABEL'))
            plt.xlabel(config.get(label, 'X_LABEL'))
            plt.title(config.get(label, 'TITLE') + " " + str(c))
            plt.xticks(rotation=config.get(label, 'ROTATION'))

            plt.show()

    def histogram_plot_from_dataframe_plotly(self, dataframe, columns, label='VISUALIZATION_HISTOGRAM_DEFAULT'):
        """
        This is a test and beta version. Only when it's enabled it would run.
        :param dataframe:
        :param columns:
        :param label:
        :return:
        """
        for c in columns:
            fig = self.px.histogram(dataframe, x=c)
            fig.show()


    def histogram_gridplot(self, dataframe, columns):
        ncols = int(config.get("PLOTS","COLUMNS"))
        total_cols = len(columns)
        if (total_cols % 2 == 0):
            nrows = total_cols // 2
        else:
            nrows = total_cols // 2

        fig, axes = plt.subplots(nrows=(nrows), ncols=ncols, figsize=(12, 15))
        r = 0
        col = 0
        for c in columns:
            try:
                axes[r][col].hist(dataframe[c])
                axes[r][col].set_title(c)
                logging.error(c)
            except Exception as e:
                pass
            finally:
                print("column :" + str(col))
                print(r)
                if (col % 2):
                    col = 0
                    r += 1
                else:
                    col += 1
        plt.show()
        plt.tight_layout()