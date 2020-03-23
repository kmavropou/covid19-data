# this script cleans the dataset provided by Johns Hopkins CSSE

import pandas as pd
import urllib.request
import os
import sys

urls = ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv',
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv',
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv']

DOWNLOADS_DIR = './'

def download_data():
    print('Downloading the most recent dataset version ...')
    for url in urls:

        name = url.rsplit('/', 1)[-1]
        filename = os.path.join(DOWNLOADS_DIR, name)

        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as inst:
            print(inst)
            print('Encountered error')
            sys.exit()

def clean():
    print('Cleaning the data ...')

    conf_df = pd.read_csv('time_series_19-covid-Confirmed.csv')
    deaths_df = pd.read_csv('time_series_19-covid-Deaths.csv')
    recv_df = pd.read_csv('time_series_19-covid-Recovered.csv')

    dates = conf_df.columns[4:]

    conf_df_long = conf_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], \
        value_vars=dates, var_name='Date', value_name='Confirmed')

    deaths_df_long = deaths_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], \
        value_vars=dates, var_name='Date', value_name='Deaths')

    recv_df_long = recv_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], \
        value_vars=dates, var_name='Date', value_name='Recovered')

    table = pd.concat([conf_df_long, deaths_df_long['Deaths'], recv_df_long['Recovered']], \
        axis=1, sort=False)

    # avoid double counting
    table = table[table['Province/State'].str.contains(',')!=True]

    # change Korea, South to South Korea
    table['Country/Region'] = table['Country/Region'].replace('Korea, South', 'South Korea')

    return table

if __name__ == '__main__':
    download_data()
    table = clean()
    table.to_csv('covid_19_clean_complete.csv', index=False)
    print('Done.')
