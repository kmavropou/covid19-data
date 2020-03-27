# this script cleans the dataset provided by Johns Hopkins CSSE

import pandas as pd
import urllib.request
import os
import sys

urls = ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv',
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv']

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

    conf_df = pd.read_csv('time_series_covid19_confirmed_global.csv', keep_default_na=False, na_values=[""])
    deaths_df = pd.read_csv('time_series_covid19_deaths_global.csv', keep_default_na=False, na_values=[""])
    recv_df = pd.read_csv('time_series_covid19_recovered_global.csv', keep_default_na=False, na_values=[""])

    dates = conf_df.columns[4:]

    conf_df_long = conf_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], \
        value_vars=dates, var_name='Date', value_name='Confirmed')

    deaths_df_long = deaths_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], \
        value_vars=dates, var_name='Date', value_name='Deaths')

    recv_df_long = recv_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], \
        value_vars=dates, var_name='Date', value_name='Recovered')

    table = pd.concat([conf_df_long, deaths_df_long['Deaths']], axis=1, sort=False)

    merge_keys = ['Province/State', 'Country/Region', 'Lat', 'Long', 'Date']
    table = pd.merge(left=table, right=recv_df_long, how='outer', left_on=merge_keys, right_on=merge_keys)

    # avoid double counting
    table = table[table['Province/State'].str.contains(',')!=True]

    # change Korea, South to South Korea
    table['Country/Region'] = table['Country/Region'].replace('Korea, South', 'South Korea')

    # sort by Date
    table['Date'] = pd.to_datetime(table['Date'])
    table = table.sort_values(by='Date')

    return table

if __name__ == '__main__':
    download_data()
    table = clean()
    table.to_csv('../output_data/covid19_clean_complete.csv', index=False)
    print(table.head())
    print('Done.')
