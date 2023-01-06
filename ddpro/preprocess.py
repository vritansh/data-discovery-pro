import matplotlib.pyplot as plt
import pandas as pd
from ddpro._readconfig import *
from ddpro.basetypes import *
__all__ = ['Preprocessor']


class Preprocessor():
    def __init__(self, df):
        """
        Constructor Configuration, dataframe and basetypes
        :param df:
        """
        self.config = config
        self.df = df
        self.basetypes = BaseTypes()

    def preprocess_dataframe(self):
        """
        Preprocess dataframe
        :return:
        """
        try:
            # Remove columns

            self.df.drop(columns=self._percentage_threshold_columns_drop(self.df), inplace=True)
            self._extract_column_types()

            return self.df, self.basetypes
        except Exception as e:
            print(e)


    def _percentage_threshold_columns_drop(self, df):
        """
        List of columns with threshold as defined
        :param self:
        :param df:
        :return:
        """
        threshold_remove_column = config.get("PREPROCESS", "MISSING_VALUES_REMOVE_THRESHOLD_PERCENT", )
        missing_values_percentage = dict(df.isnull().sum().sort_values(ascending=False) * 100 / len(df))
        columns_to_remove = {k: v for k, v in missing_values_percentage.items() if v >= float(threshold_remove_column)}
        return list(columns_to_remove.keys())


    def _extract_column_types(self):
        """
        Sets the basetype of the classes to numerical and categorical columns accordingly
        :return:
        """
        try:
            all_types = config.items('DATA_TYPES')
            column_types_mapping = {}
            for types in all_types:
                if (types[0] == 'continuous'):
                    self.basetypes.numerical = set(self.df.select_dtypes(include=types[1]).columns)
                if (types[0] == 'categorical'):
                    self.basetypes.categorical = set(self.df.select_dtypes(include=types[1]).columns)


            #Extract actual numerical variables from the dataset by removing the target variable
            #Remove all target variables with less than threshold categories
            #threshold
            categories_threshold = self.config.get("THRESHOLD","CATEGORIES_THRESHOLD")
            numerical_columns = list(self.basetypes.numerical)
            id_types = set()
            for c in numerical_columns:

                #Remove columns with specified threshold for categories added in numerical variables
                if(self.df[c].nunique() < int(categories_threshold)):
                            self.basetypes.numerical.remove(c)

                #Remove columns with Only IDs. If the number of unique elements is equal to total number of elements
                if(self.df[c].nunique() == len(self.df)):
                             self.basetypes.numerical.remove(c)
                             id_types.add(c)
            self.basetypes.id= id_types



        except Exception as e :
            print(e)
            raise Exception(e)


    def _calculate_technical_indicators(self, columns):
        technical_indicator ={}
        all_technical_indicators = []
        try:
            for c in columns:
                for c in self.df.columns:
                    technical_indicator = dict(self.df[c].describe())
                    technical_indicator['column'] = c
                    all_technical_indicators.append(technical_indicator.copy())
        except Exception as e :

            raise Exception(e)










