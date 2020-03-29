import os
import urllib.request
import sys

DOWNLOADS_DIR = './'

out_filename = 'COVID_open_line_list_data.csv'

source_url = 'https://raw.githubusercontent.com/beoutbreakprepared/nCoV2019/master/latest_data/latestdata.csv'

print('Downloading data ...')

filename = os.path.join(DOWNLOADS_DIR, out_filename)

try:
    urllib.request.urlretrieve(source_url, filename)
except Exception as inst:
    print(inst)
    print('Encountered error')
    sys.exit()

print('Done.')
