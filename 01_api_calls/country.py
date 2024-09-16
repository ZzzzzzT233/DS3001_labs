import urllib.request
import json
import pandas as pd
import streamlit as st
url = 'https://www.saferproducts.gov/RestWebServices/' # Location of the API
query = 'Recall?format=json&ProductType=Exercise' # The query
response = urllib.request.urlopen(url+query)
response_bytes = response.read()
data = json.loads(response_bytes) # Convert response to json
response.close()

df = pd.DataFrame.from_dict(data)

temp = df['ManufacturerCountries']
clean_values = []
for i in range(len(temp)):
    if len(temp[i])>0:
        values = []
        for j in range(len(temp[i])):
            values.append(temp[i][j]['Country'])
        clean_values.append(values)
    else:
        clean_values.append('')
df['country'] = clean_values
print(df['country'].value_counts())
print(df['country'].describe(), '\n')
country_count = df['country'].value_counts
st.title('Country Statistics')
st.write('Summary Statistics:')
st.write(df['country'].describe()) 