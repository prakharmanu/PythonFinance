import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web
import pandas as pd

style.use("ggplot")

# start = dt.datetime(2015,1,1)
# end = dt.datetime(2020,1,1)
#
# df = web.DataReader("TSLA", "yahoo", start, end)
#
# df.to_csv('TslaStock')


df = pd.read_csv('TslaStock', parse_dates=True, index_col=0)
print(df[['Open','High']].head())
df.plot()
plt.show()