import matplotlib.pyplot as plt
from ddpro._readconfig import *
import plotly.express as px
import seaborn as sns
import scipy.stats as stats

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

    def box_plot_from_dataframe(self, dataframe, columns, label='VISUALIZATION_HISTOGRAM_DEFAULT'):
        """
        This method plots a histogram for best describing the distribution of the data. It is run after cleaning the dataset
        :param data_dict:
        :param label:
        :return:
        """
        if (len(dataframe) == 0):
            return
        for c in columns:
            plt.boxplot(dataframe[c])

            plt.ylabel(config.get(label, 'Y_LABEL'))
            plt.xlabel(config.get(label, 'X_LABEL'))
            plt.title(config.get(label, 'TITLE') + " " + str(c))
            plt.xticks(rotation=config.get(label, 'ROTATION'))

            plt.show()

    def qqplot_from_dataframe(self, dataframe, columns):
        print("logging infor")
        for c in columns:
            stats.probplot(dataframe[c], dist="norm", plot=plt)
            plt.title('Q-Q Plot for normality')
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

    def histogram_grid(self, dataframe, columns):
        """
        Generate histogram from dataframe and column names
        :param dataframe:
        :param columns:
        :return:
        """
        total_cols = len(columns)
        fig, axes = self._get_axes_dimensions(total_cols)
        if fig == None and axes == None:
            return
        row = 0
        col = 0
        for c in columns:
            try:
                title = "Distribution of column " + str(c)
                if ( total_cols <= 2 ):
                    axes[col].hist(dataframe[c], color='c', bins =5)
                    axes[col].set_title(title)
                else:
                    axes[row][col].hist(dataframe[c])
                    axes[row][col].set_title(title)
            except Exception as e:
                print(e)
                logger.error(e)
            finally:
                if (col % 2):
                    col = 0
                    row += 1
                else:
                    col += 1

        plt.show()
        fig.suptitle(config.get("PLOTS", "TITLE_DISTRIBUTION"))
        plt.tight_layout()

    def boxplot_grid(self, dataframe, columns):
        """
        Generate boxplot from dataframe and column names
        :param dataframe:
        :param columns:
        :return:
        """
        total_cols = len(columns)
        fig, axes = self._get_axes_dimensions(total_cols)

        if fig == None and axes == None:
            return

        row = 0
        col = 0
        for c in columns:
            try:
                title = "Distribution of column "+str(c)
                if (2 >= len(columns)):
                    axes[col].boxplot(dataframe[c], vert=False)
                    axes[col].set_title(title)
                else:
                    axes[row][col].boxplot(dataframe[c], vert=False)
                    axes[row][col].set_title(title)
            except Exception as e:
                logger.error(e)
            finally:

                if (col % 2):
                    col = 0
                    row += 1
                else:
                    col += 1

        plt.show()
        fig.suptitle(config.get("PLOTS", "TITLE_DISTRIBUTION"))
        plt.tight_layout()

    def pairplot_from_dataframe(self, dataframe, columns):
        sns.pairplot(dataframe[columns])
        plt.show()

    def _get_axes_dimensions(self, total_cols):
        """
        Generate gridspace for total plots that  are required
        :param columns:
        :return:
        """
        fig = axes = None
        try:
            ncols = int(config.get("PLOTS", "COLUMNS"))
            nrows = 1
            # Calculate the number of rows and columns
            if (total_cols > 2):
                if total_cols % 2 == 0:
                    nrows = total_cols // total_cols
                else:
                    nrows = total_cols // total_cols + 1

            fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(7, 5))
            print(axes.shape)
            return fig, axes
        except Exception as e:
            logger.error(e)
        finally:
            return fig, axes
