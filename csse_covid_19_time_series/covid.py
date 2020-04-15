import pandas as pd

#4

def correctDateFormat(df):
    df = df.melt(id_vars=df.columns[0:4], var_name="Date", value_name="Confirmed")

#6

    df["Data"] = pd.to_datetime(df["Date"])
    return df

# 14

def aggregateCountry(df, country):
    data = df.loc[df["Country/Region"] == country]
    return data.groupby("Date", as_index=False).sum()

# 15

def topCorrelation(df, country):
    corrs = []
    countries = pd.unique(df["Country/Region"])
    repeat = []
    for c1 in countries:
        for c2 in countries:
            if c1 != c2:
                if[c1, c2] not in repeat and [c2, c1] not in repeat:
                    c1Data = df.loc[df["Country/Region"] == c1]
                    c1Data = df.groupby("Date", as_index = False).sumn()

                    x = c1Data["Confirmed"].sum()
                    c2Data = df.loc[df["Country/Region"] == c2]
                    c2Data = df.groupby("Date", as_index = False).sum()

                    y= c2Data["Confirmed"].sum()
                    if (c1Data["Confirmed"]).sum() >= 500 and c2Data["Confirmed"].sum()) >= 500):
                        return c1Data[topColumn].corr(c1Data[topColumn])
