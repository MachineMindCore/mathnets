import requests
import json
import os

def download_pipeline():
    NATURALPROOFS_PROOFWIKI_SOURCE = "https://zenodo.org/record/4902289/files/naturalproofs_proofwiki.json?download=1"
    byte_data = requests.get(NATURALPROOFS_PROOFWIKI_SOURCE, allow_redirects=True).content
    decoded_json = byte_data.decode('utf8').replace("'", '"')
    data = json.loads(decoded_json)

    os.mkdir("donwload/")
    with open('download/naturalproofs_proofwiki.json', 'w') as f:
        json.dump(data, f, indent=4)
    