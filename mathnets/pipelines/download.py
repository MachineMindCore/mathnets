import urllib3
import os

def download_pipeline():
    NATURALPROOFS_PROOFWIKI_SOURCE = "https://zenodo.org/record/4902289/files/naturalproofs_proofwiki.json?download=1"
    
    print("########## DOWNLOAD ##########")
    print("----> downloading json file")
    http = urllib3.PoolManager()
    response = http.request('GET', NATURALPROOFS_PROOFWIKI_SOURCE)
    data = response.data

    print("----> saving")
    os.mkdir("download/")
    file_name = 'download/naturalproofs_proofwiki.json'
    with open(file_name, 'wb') as file:
        file.write(data)