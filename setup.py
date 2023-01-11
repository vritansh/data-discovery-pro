from os import path
from setuptools import setup
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
# encoding is not supported in py27
# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
setup(
    name='ddpro',
    version='0.0.2',
    description='Data Discovery Pro for Automated EDA and ML',
    author='Vritansh Kamal',
    author_email='vritansh14@gmail.com',
    license='MIT',
    packages=['ddpro'],
    package_data={'ddpro': ['config/*',]},
    keywords='machine-learning data-science jupyter-notebook',
    install_requires=[
      'pandas', 'numpy', 'seaborn', 'matplotlib',
      'sklearn', 'future', 'configparser'
    ],
    zip_safe=False,
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[

        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
 )
