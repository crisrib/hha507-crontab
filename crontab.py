# Import packages
import crontab
import os
import requests
import sys
import time
import pandas as pd
import airflow

# Import dataframe
df = pd.read_json('https://data.covid19india.org/v4/min/data.min.json')
df

# Save dataframe as csv
df.to_csv('COVID19daily.csv', index = None)

# Get system timestamp
currentTime = time.time()
listTime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(currentTime))
print('The current time is: ', listTime)

# Get cwd
cwd = os.getcwd()
print(cwd)

## Create file in cwd
with open(cwd + '/updateFile_' + listTime + '.txt', 'w') as f:
    f.write(str(df))