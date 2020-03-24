# this script converts the data from Johns Hopkins CSSE into a JSON file

import pandas as pd
import json

def export_to_json(data, filename):
    json_output = '{'
    for name, group in data.groupby(["Country/Region"]):
        json_output += ('\n\t"' + name + '": [')
        for index, row in group.iterrows():
            json_output += '\n\t\t{\n\t\t\t'

            json_output += ('"date": "' + str(index[1])[:-9] + '",')
            json_output += ('\n\t\t\t"confirmed": ' + str(int(row['Confirmed'])) + ',')
            json_output += ('\n\t\t\t"recovered": ' + str(int(row['Recovered'])) + ',')
            json_output += ('\n\t\t\t"deaths": ' + str(int(row['Deaths'])))
            json_output += '\n\t\t},'

        json_output = json_output[:-1]
        json_output += '\n\t],'
    json_output = json_output[:-1]
    json_output += '\n}\n'


    with open(filename, 'w') as outfile:
        outfile.write(json_output)


if __name__ == '__main__':
    data = pd.read_csv('../output_data/covid19_clean_complete.csv')

    data = data.drop(columns=["Province/State", "Lat", "Long"])

    data['Date'] = pd.to_datetime(data['Date'])
    data = data.groupby(["Country/Region", "Date"])["Confirmed", "Deaths", "Recovered"].sum()

    export_to_json(data, '../output_data/timeseries_per_country.json')
