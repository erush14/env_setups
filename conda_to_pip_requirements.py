#turn conda requirements to pip requirements.txt
#bc im not doing this by hand
import re
import pandas as pd


conda_req = pd.read_csv('requirements.txt', skiprows=2, sep='\s{2,}', engine='python')
conda_req.columns = ['conda_col']
conda_req['pip_column'] = conda_req['# Name']+'=='+conda_req['Version']
conda_req['pip_column'].to_csv('pipreqs.txt', header=None, index=None, sep=' ', mode='a')
