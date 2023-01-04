import configparser
import os
import configparser

config = configparser.ConfigParser()



def initial_setup():
    config = configparser.ConfigParser()
    ini_path = os.path.join(os.getcwd(), 'config.ini')
    config.read(ini_path)
    return config
