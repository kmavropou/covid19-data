import os
import urllib.request
import sys

DOWNLOADS_DIR = './'

out_format = 'csv'
out_filename = 'COVID19_line_list_data'

source_url = 'https://docs.google.com/spreadsheets/d/1jS24DjSPVWa4iuxuD4OAXrE3QeI8c9BC1hSlqr-NMiU/gviz/tq?tqx=out:' + \
    out_format + '&sheet=' + out_filename

print('Downloading data ...')

filename = os.path.join(DOWNLOADS_DIR, out_filename + '.' + out_format)

try:
    urllib.request.urlretrieve(source_url, filename)
except Exception as inst:
    print(inst)
    print('Encountered error')
    sys.exit()

print('Done.')
