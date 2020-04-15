from utils import *
from covid import *

#3

df = loadAndCleanData("time_series_covid19_confirmed_global.csv")

#5

df = correctDateFormat(df)
print(df)

x = "Date"
y = "Confirmed"

#7

df1 = loadAndCleanData("time_series_covid19_deaths_global.csv")
df2 = loadAndCleanData("time_series_covid19_recovered_global.csv")

# 9

print(mergeData(df, df1, "Deaths"))
x = mergeData(x, df2, "Recovered")
print(mergeData(x, df2, "Recovered"))

#11

plotTimeline(x, "Date", "Confirmed")
plotTimeline(x, "Date", "Deaths")
plotTimeline(x, "Date", "Recovered")

# 13

plotMultipleTimeLines(x, "Date", "Recovered", "Deaths")
plotMultipleTimeLines(x, "Date", "Confirmed", "Deaths")
plotMultipleTimeLines(x, "Date", "Confirmed", "Recovered")

# 16

topCorrelation(x, "Confirmed")
