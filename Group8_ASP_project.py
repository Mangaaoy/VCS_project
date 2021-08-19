import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import group8_python_unittest as prog

file= pd.read_excel('IMVA.xls',sheet_name='IMVA')
fileSplit = file['Periods'].str.split(' ', n=1, expand=True)
file = file.assign(Year=(fileSplit[0]))
europedata = file[((file['Year'] >= str(1998)) & (file['Year'] <= str(2007)))]
europeFilter = europedata.filter(items=["Belgium & Luxembourg", "Denmark", "Finland", "France", "Germany", "Italy", "Netherlands", "Norway",
               "Rep Of Ireland", "Russian Federation", "Spain", "Sweden", "Switzerland", "United Kingdom"])

print(europeFilter)

print("***************** First 3 in 1998 **************")
data_top = europedata.loc[242:244]
print(data_top)

print("***************** Last 3 in 2007 ***************")
data_bottom = europedata.loc[357:359]
print(data_bottom)

europedata2 = file[["Belgium & Luxembourg", "Denmark", "Finland", "France", "Germany", "Italy", "Netherlands", "Norway",
               "Rep Of Ireland", "Russian Federation", "Spain", "Sweden", "Switzerland", "United Kingdom"]]
europedata2 = europedata2.replace(',','', regex=True)
europedata2 = europedata2.replace('na', '0', regex=True)
print(europedata2)

europedata3 = europedata2.astype(int)
print(europedata3.dtypes)

print("**************** Unsorted ***************")
psNotSorted = europedata3.sum()
print(psNotSorted)

print("**************** Sorted *****************")
psSorted = psNotSorted.sort_values(ascending=False)
print(psSorted)

print("**************** TOP 3 COUNTRIES *************")
data_top2 = psSorted.head(3)
print(data_top2)

print("**************** SUM OF THE 3 COUNTRIES ****************")
totaldata_top2 = psSorted.head(3).sum()
print(" ".join(["The total sum of top 3 countries is", str(totaldata_top2)]))

print("**************** MEAN OF THE 3 COUNTRIES ****************")
mean = round(totaldata_top2/3 , 2)
print(" ".join(["The mean of top 3 countries is", str(mean)]))


frame = pd.DataFrame(europeFilter)
frame = frame.assign(Year=(fileSplit[0]))
frame.index = frame['Year']
del frame['Year']
frame = frame.replace(',', '', regex=True)
frame = frame.replace('na', '0', regex=True)
frame = frame.astype(int)
totalframe = frame.sum(axis=0)
totalframe = totalframe.sort_values(ascending=False)

("****************** GRAPH 1 ***************")
frame2 = pd.DataFrame(totalframe)
frame2 = frame2.assign(Country=(frame2.index))
frame2 = frame2.assign(Total=(frame2[0]))
del frame2[0]
ps = frame2['Total'].sort_values(ascending=False) / 1000
index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=15)
plt.ylabel('Total amount of Travellers (in thousands)', fontsize=10, rotation=90)
plt.xticks(index, (ps.index), fontsize=10, rotation=90)
plt.title('All countries from 1998-2007')
plt.bar(ps.index, ps.values)
plt.tight_layout()
plt.show()

("****************** GRAPH 1 ***************")
frame2 = frame2.head(3)
ps = frame2['Total'].sort_values(ascending=False) / 1000
index = np.arange(len(ps.index))
plt.xlabel('Countries', fontsize=15)
plt.ylabel('Total amount of Travellers (in thousands)', fontsize=10, rotation=90)
plt.xticks(index, (ps.index), fontsize=10, rotation=90)
plt.title('All countries from 1998-2007')
plt.bar(ps.index, ps.values)
plt.tight_layout()
plt.show()