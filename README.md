<h1> ddpro - Data Discovery Pro </h1>

Release : Planning [ Bug Fixes in Progress ]

Update <>  22nd May 2023 - This repo would have another update soon. 
Below reseleases are targetted :

https://pypi.org/project/ddpro

Bored with writing code for EDA and building pipelines for every dataset ? Wish if there was on stop solution for it. Presenting Data Discovery Pro ( Pro ?? Nope!  you don't need a credit card  ). 

This library provides handy methods to generate Plots describing the distribution, normality and the bias in the dataset. Just drop in the data and provide the target column. Internally it uses Pandas dataframe to perform operations. Currently supporting ".json", ".csv" files. Will expand to complete support by pandas.

Currenlty Supported:
1. Distribution Plots - Histograms, QQ Plot
2. Extraction of Categorical and Numerical columns. Total number of categorical columns have been capped in config.ini file
3. Plot Target variables distribution
4. Automated 'na' and 'isnull' operations on the dataset
5. Plot Target variables distribution after removal 

Next release - Method names would be in sync with other popular libraries like - pandas. 

Future:
AutomL
Hypothesis Testing
Deployment to AWS 

Installation
To install ddpro, simply use pip:

pip install ddpro

Usage
import ddpro

# Load your data
df = ddpro.DdPro('my_data.csv','target_column', Options)

# Perform EDA
eda_report = ddpro.generate_plots(df)


Contributing
We welcome contributions to the ddpro library! If you'd like to contribute, please follow these steps:

Fork the repository
Create a new branch for your changes
Make your changes
Submit a pull request

🙌 Thank you for considering contributing to ddpro! 🙌
