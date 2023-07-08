import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import dropbox

access_token = 'sl.Bh2jNEskaLx_3TXNgkXJRGAyT0laW4NFRcdsWAqTQFUliCqE2Ei8sHurBw0_MyQns3g1-sDbvmNJ0fVvpNMNZFeYOL9t-Ue98nR2HPKwpg6NeKq2TQQd6fJ1tk8XIRRheaMXf6u7HlGp'
client = dropbox.Dropbox(access_token)

# from openpyxl.utils import datetime
df = pd.read_excel('example_modified_copy.xlsx')
df_interpol = df.groupby('asset_serial_number').resample('2min',on='record_create_timestamp').mean()
df_interpol.reset_index(inplace=True)
df_interpol['state_of_charge'] = df_interpol['state_of_charge'].interpolate(method='spline',order=1)
# df_interpol['record_create_timestamp'] = df_interpol['record_create_timestamp'].interpolate('linear')
print(df_interpol.head(200))
# df_interpol.to_csv('new_ans.csv',index=False)

# df_interpol.head(200).to_excel('new_ans.xlsx')
df_interpol.to_excel('new_ans.xlsx')
df1=pd.read_excel('new_ans.xlsx')

# df.sample(100)
graph1 = df1[df1['asset_serial_number']=="ASN00003"]  # Replace 'Column_Name' with the actual column name and set your desired condition
graph2 = df1[df1['asset_serial_number']=="ASN00004"] 

g1_x=graph1['record_create_timestamp']
g1_y=graph1['state_of_charge']
g2_x=graph2['record_create_timestamp']
g2_y=graph2['state_of_charge']
plt.title("For every minutes")
plt.plot(g1_x,g1_y, color="blue", linewidth=2)
plt.plot(g2_x,g2_y, color="red", linewidth=2)
fig1=plt.gcf()
# plt.show()
fig1.savefig('graph.jpeg')

# Upload the graph file to Dropbox
with open('graph.jpeg', 'rb') as file:
    client.files_upload(file.read(), '/graph.jpeg' )














# filtered_df = df1[df1['state_of_charge'] >= 100]  # Replace 'Column_Name' with the actual column name and set your desired condition

# # Display the filtered rows
# print(filtered_df)