import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import seaborn as sns
from datetime import datetime

data = pd.read_csv('../output_data/covid19_clean_complete.csv', keep_default_na=False, na_values=[""])
data['Date'] = pd.to_datetime(data['Date'])
data['Date'] = data['Date'].map(lambda t: t.strftime('%Y-%m-%d'))
daily_data = data.groupby(["Date"])["Confirmed", "Deaths", "Recovered"].sum()
data.set_index(['Date'],inplace=True)

for col in daily_data.columns:
    daily_data[col] = daily_data[col].apply(lambda x: int(x))

# plot worldwide total cases
sns.set(color_codes=True)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

fig, ax = plt.subplots(figsize=(15,8))
daily_data.plot(ax=ax, marker='o', markersize=4)

ax.set_title('Worldwide total reported COVID-19 cases')
ax.set_xlabel("Date")
ax.set_ylabel("Total cases")

fig.savefig('../docs/images/worldwide_total_cases.png')
plt.show()
