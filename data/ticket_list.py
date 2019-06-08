import requests
import json
import pandas as pd

response = requests.get('https://{subdomain}.zendesk.com/api/v2/tickets.json', auth=({username}, {password}))
response_text = response.text #Convert 'Response' to text.

list_data_dict = json.loads(response_text)
list_data = list_data_dict['tickets']

df = pd.DataFrame(list_data) #Convert dict into dataframe
df.reset_index(level=0, inplace=True)

to_display = df[['id', 'subject', 'status', 'priority']]
print(to_display)
