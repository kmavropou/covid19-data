import os
import urllib.request
import sys
import progressbar

DOWNLOADS_DIR = './data/'
out_filename = 'covid-chestxray-dataset.zip'

source_url = 'https://github.com/ieee8023/covid-chestxray-dataset/archive/master.zip'

# Progress bar
pbar = None
downloaded = 0

def show_progress(block_num, block_size, total_size):
    global pbar, downloaded
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()

def download():
    print('Downloading data ...')

    if not os.path.exists(DOWNLOADS_DIR):
        os.makedirs(DOWNLOADS_DIR)

    filename = os.path.join(DOWNLOADS_DIR, out_filename)

    try:
        urllib.request.urlretrieve(source_url, filename, reporthook=show_progress)
    except Exception as inst:
        print(inst)
        print('Encountered error')
        sys.exit()

    print('Done.')

if __name__ == '__main__':
    download()
