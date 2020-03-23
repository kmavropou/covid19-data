import os
import urllib.request
import sys

DOWNLOADS_DIR = './'

print('Downloading data ...')

for url in open('urls.txt'):

    name = url.rsplit('/', 1)[-1].strip()
    filename = os.path.join(DOWNLOADS_DIR, name)

    try:
        urllib.request.urlretrieve(url, filename)
    except Exception as inst:
        print(inst)
        print('Encountered error')
        sys.exit()

print('Done.')
