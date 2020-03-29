import os
import urllib.request
import sys

DOWNLOADS_DIR = './'

out_format = 'csv'
out_filename = 'data'

source_url = 'https://docs.google.com/spreadsheets/d/14quQPFErG-hlpsrNgYcX85vW7JMMK5X2vNZrafRcH8c/gviz/tq?tqx=out:' + \
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
