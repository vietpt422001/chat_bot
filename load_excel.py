import pandas as pd

def getColomnValue(indexOfcolumn=2,folderName = "Ref/input.csv"):

    df = pd.read_csv(folderName)
    data = df[df.columns[indexOfcolumn]]
    data1 = []
    for i in range(len(data.index)):
        data1.append(data.iloc[i])
    return data1


