import configparser
import os
import logging

config = configparser.ConfigParser()
log = None


__all__ = ['config','initial_setup']


def initial_setup(override=False, file_name='config.ini', path=None):
    """
    Override the configuration by providing your own
    :param path:
    :param override:
    :param file_name:
    :return: """
    if not override:
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    else:
        config_path = os.path.join(path, file_name)
    config.read(config_path)

    #Get the Logger file name and debug level
    log= logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.ERROR)