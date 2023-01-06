import configparser
import os
import logging

config = configparser.ConfigParser()
logging.basicConfig(
    filename='server.log',
    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(pathname)s:%(lineno)d in ' \
           'function %(funcName)s] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.ERROR
)

logger = logging.getLogger(__name__)
__all__ = ['config','initial_setup','logger']


def initial_setup(override=False, file_name='config.ini', path=None):
    """
    Override the configuration by providing your own
    :param path:
    :param override:
    :param file_name:
    :return: """
    if not override:
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config',file_name)
    else:
        config_path = os.path.join(path, file_name)
    config.read(config_path)