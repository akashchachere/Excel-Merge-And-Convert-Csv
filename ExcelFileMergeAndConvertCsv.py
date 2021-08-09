import pandas as pd
import glob
import os
#file path
path = r"C:\\Users\\sony\\Desktop\\Excel Sheet\\Example.xlsx"
filename = glob.glob(path)
a = pd.DataFrame()
for file in filename:
    df = pd.read_excel(file,sheet_name=None,skiprows=None,nrows=None,usecols=None,header=None,index_col=None)
    b = pd.concat(df,sort=False)
    b[filename] = os.path.basename(file)

    a = b.append(b)

writer = pd.ExcelWriter(r"C:\\Users\\sony\\Desktop\\Excel Sheet\\MasterFile.xlsx")
a.to_excel(writer,index=True,header=False)
writer.save()
#Excel File Convert to Csv
a.to_csv("C:\\Users\\sony\\Desktop\\Excel Sheet\\MeargeFile.csv",index=True,header=True)
print(a)

