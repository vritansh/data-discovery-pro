from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
from ddpro.basetypes import BaseTypes
from ddpro.plot import *

from ddpro._readconfig import config
import configparser
import os
import pandas as pd
import numpy as np
import pathlib
from ddpro._readconfig import *
from ddpro.preprocess import *
from ddpro.preprocess import *


class DdPro():
    def __init__(self, data_source, target_column, options):
        """
        Open datasets ``train`` and ``test`` as CSV or JSON files and store in pandas DataFrames ``Base.train`` and ``Base.test``. Set ``Base.target`` and ``Base.uid`` values based on parameters. Initialize ``Plot``, ``Feature``, and ``Xgb`` components.
        """
        initial_setup()
        self.basetypes = BaseTypes()
        self.plot = Visualize()

        if (self._verify_extensions(data_source)):
            self.DataSource = data_source
            self.Options = options
            self.target_column = target_column
            self.df = self._convert_to_dataframe()
            # self._raw_data_exploration()
            # Missing values Barplot
            self._raw_data_visualization()
            self._data_visualization()

    def _verify_extensions(self, data):
        """
        Verify extensions exist in the list of allowed file extensions. Defined in config.ini
        """
        if data.endswith(tuple(config.get('FILE_EXTENSIONS', 'ALLOWED_FILE_EXTENSIONS'))):
            return True
        else:
            raise Exception(f'File type {data} is not supported')

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
            Showcase how the data looks like in the EDA
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
        preprocesor = Preprocessor(self.df)
        self.df, self.basetypes = preprocesor.preprocess_dataframe()
        # self.plot.histogram_plot_from_dataframe_plotly(self.df,
        #                                        self.basetypes.numerical)

        self.plot.histogram_gridplot(self.df, self.basetypes.numerical)

test = DdPro('titanic.csv','Survived', 'random')
