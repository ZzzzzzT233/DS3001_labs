import urllib.request
import json
import pandas as pd
import numpy as np
import streamlit as st

url = 'https://api.eia.gov/v2/aeo/2023/data/'
api_key = 'api_key=DhdmbI8p175jM5zjZQQ37ofzruRfqdM8TgpuLBcz'
query = 'frequency=annual&data[0]=value&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'

response = urllib.request.urlopen(url+"?"+api_key+"&"+query)
response_bytes = response.read()
data = json.loads(response_bytes) # Convert response to json
response.close()

df = pd.DataFrame.from_dict(data['response']['data'])


temp = df['regionName']
temp = temp.replace('No Regional Tables',np.nan)

print(temp.value_counts())
print(temp.describe())
df['regionName'] = temp
del temp

st.title('Region Statistics')
st.write('Count Statistics:')
st.write(df['regionName'].value_counts()) 

st.write('Summary Statistics:')
st.write(df['regionName'].describe()) 







