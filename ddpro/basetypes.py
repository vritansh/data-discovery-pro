from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

__all__ = ['BaseTypes']
class BaseTypes:
    def __init__(self, numerical=None, categorical=None):
        self.numerical = numerical
        self.categorical = categorical

