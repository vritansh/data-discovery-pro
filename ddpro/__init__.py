# from __future__ import (absolute_import, division,
#                         print_function, unicode_literals)

import sys
import logging
import os

from ddpro._readconfig import initial_setup,config
from ddpro.main import DdPro

def __init__(self):
        initial_setup()
        print(config)



# from builtins import *
# from .basetypes import BaseTypes
# from .plot import Visualize
# from ._readconfig import initial_setup,config
# import configparser
# import os
# import pandas as pd
# import numpy as np
# import pathlib
#
#
#
# class DdPro():
#     def __init__(self, data_source, target_column, options):
#         """
#         Open datasets ``train`` and ``test`` as CSV or JSON files and store in pandas DataFrames ``Base.train`` and ``Base.test``. Set ``Base.target`` and ``Base.uid`` values based on parameters. Initialize ``Plot``, ``Feature``, and ``Xgb`` components.
#         """
#         initial_setup()
#         self.basetypes = BaseTypes()
#         self.plot = Visualize()
#
#         if (self._verify_extensions(data_source)):
#             self.DataSource = data_source
#             self.Options = options
#             self.target_column = target_column
#             self.raw_df = self._convert_to_dataframe()
#             self._raw_data_exploration()
#             # Missing values Barplot
#             self._raw_data_visualization()
#             self._extract_columns_types()
#
#     def _verify_extensions(self, data):
#         """
#         Verify extensions exist in the list of allowed file extensions. Defined in config.ini
#         """
#         if data.endswith(tuple(config.get('FILE_EXTENSIONS', 'ALLOWED_FILE_EXTENSIONS'))):
#             return True
#         else:
#             raise Exception(f'File type {data} is not supported')
#
#     def _convert_to_dataframe(self):
#         """
#         Read the files generically using Pandas read_* method. It would translate based on file extension type
#         """
#         df = pd.DataFrame
#         try:
#             method_name = 'read' + "_" + pathlib.Path(self.DataSource).suffix[1:]
#             df = getattr(pd, method_name)(self.DataSource)
#         except Exception as e:
#             raise Exception(e)
#         finally:
#             return df
#
#
#     def _raw_data_exploration(self):
#         """"
#             Showcase how the data looks like in the EDA
#         """
#         df = self.raw_df
#         print("** Head **")
#         print(df.head())
#         print("** Shape **")
#         print(df.shape)
#         print("** Describe **")
#         print(df.describe())
#         print("** Columns **")
#         print(df.columns)
#
#     def _extract_columns_types(self):
#         """
#         Sets the basetype of the classes to numerical and categorical columns accordingly
#         :return:
#         """
#         all_types = config.items('DATA_TYPES')
#         for types in all_types:
#             if (types[0] == 'continuous'):
#                 self.basetypes.numerical = self.raw_df.select_dtypes(include=types[1]).columns.tolist()
#                 print(self.basetypes.numerical)
#             if (types[0] == 'categorical'):
#                 self.basetypes.numerical = self.raw_df.select_dtypes(include=types[1]).columns.tolist()
#
#     def _raw_data_visualization(self):
#         missing_values = dict(self.raw_df.isnull().sum().sort_values(ascending=False))
#         # Handle missing values here
#         self.plot.bar_plot_from_dict(missing_values, 'VISUALIZATION_BAR_PLOT_MISSING')
#         # Plot target variable distribution
#         target_values = dict(self.raw_df[self.target_column].value_counts())
#         self.plot.bar_plot_from_dict(target_values, 'VISUALIZATION_BAR_PLOT_TARGET')
#
#
# s = DdPro('titanic.csv', 'Survived', 'sample')
