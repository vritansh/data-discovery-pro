from os import path
from setuptools import setup
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
# encoding is not supported in py27
# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:

setup(
    name='ddpro',
    version='0.0.1',
    description='Data Discovery Pro for Automated EDA and ML',
    author='Vritansh Kamal',
    author_email='vritansh14@gmail.com',
    license='MIT',
    packages=['ddpro'],
    keywords='machine-learning data-science jupyter-notebook',
    install_requires=[
      'pandas', 'numpy', 'seaborn', 'matplotlib',
      'sklearn', 'future', 'configparser'
    ],
    zip_safe=False,
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 2 - Pre-Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
 )
