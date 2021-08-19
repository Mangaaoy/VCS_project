import pandas as pd
file= pd.read_excel('IMVA.xls',sheet_name='IMVA')
print(file)

files=file['Periods'].str.split(' ',n=1,expand=True)
print(files)

print("Summarize the first 100 columns")
print(file.iloc['Belgium & Luxembourg','Denmark','Finland','France','Germany','Italy','Netherlands','Norway','Rep of Ireland',
      'Russian Federation','Spain','Sweden','Switzerland','United Kingdom'].describe())