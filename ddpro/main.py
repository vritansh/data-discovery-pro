from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
from ddpro.basetypes import BaseTypes
from ddpro.plot import *

import pandas as pd
import pathlib
from ddpro._readconfig import *
from ddpro.preprocess import *

class DdPro():
    def __init__(self, data_source, target_column, options):
        """
        Intialize data. Replace this method with load_dataset
        """
        initial_setup()
        self.basetypes = BaseTypes()
        self.plot = Visualize()

        if (self._verify_extensions(data_source)):
            self.DataSource = data_source
            self.Options = options
            self.target_column = target_column
            self.df = self._convert_to_dataframe()

        else:
            raise Exception(f"{data_source} does not exist in list of allowed extensions")

    def _verify_extensions(self, data_source):
        """
       Verify extensions exist in the list of allowed file extensions. Defined in config.ini
       :param data_source:
       :return:
       """
        if data_source.endswith(tuple(config.get('FILE_EXTENSIONS', 'ALLOWED_FILE_EXTENSIONS'))):
            return True
        else:
            return False

    def _convert_to_dataframe(self):
        """
        Read the files generically using Pandas read_* method. It would translate based on file extension type
        """
        df = pd.DataFrame
        try:
            method_name = 'read' + "_" + pathlib.Path(self.DataSource).suffix[1:]
            df = getattr(pd, method_name)(self.DataSource)
        except Exception as e:
            raise Exception(e)
        finally:
            return df

    def _raw_data_exploration(self):
        """"
            Showcase how the data looks like in text format
        """
        df = self.df
        print("** Head **")
        print(df.head())
        print("** Shape **")
        print(df.shape)
        print("** Describe **")
        print(df.describe())
        print("** Columns **")
        print(df.columns)

    def _raw_data_visualization(self):
        missing_values = dict(self.df.isnull().sum().sort_values(ascending=False))
        # Handle missing values here
        self.plot.bar_plot_from_dict(missing_values, 'VISUALIZATION_BAR_PLOT_MISSING')
        # Plot target variable distribution
        target_values = dict(self.df[self.target_column].value_counts())
        self.plot.bar_plot_from_dict(target_values, 'VISUALIZATION_BAR_PLOT_TARGET')

    def _data_visualization(self):
        """
        This method preprocesses and calls relevant visualization. Curently only supports matplotlib.
        Future - Add support for plotly
        :return:
        """
        # Visualize raw data before cleaning
        self._raw_data_visualization()
        preprocesor = Preprocessor(self.df)
        self.df, self.basetypes = preprocesor.preprocess_dataframe()
        print("Categorical Columns : ", self.basetypes.categorical)
        print("Categorical Columns : ",self.basetypes.numerical)

        if (config.get("THEME", "LIBRARY") == 'matplotlib'):
            self._matplotlib_visualization()
        else:
            raise Exception("Only matplotlib is supported")

    def _matplotlib_visualization(self):
        """
        Create visualizations related to matplotlib
        :return:
        """
        # Single plots vs grid plots based on the data
        # Distribution Related Plots for Normality
        if (len(self.basetypes.numerical) <= 2):
            self.plot.histogram_grid(self.df, self.basetypes.numerical)
            self.plot.boxplot_grid(self.df, self.basetypes.numerical)
            self.plot.qqplot_from_dataframe(self.df, self.basetypes.numerical)
        # else:
        #     self.plot.histogram_plot_from_dataframe(self.df, self.basetypes.numerical)
        #     self.plot.box_plot_from_dataframe(self.df, self.basetypes.numerical)


        #Correlation between multiple variables
        self.plot.pairplot_from_dataframe(self.df, self.basetypes.numerical)

    def discover(self):
            self._raw_data_exploration()
            self._data_visualization()

