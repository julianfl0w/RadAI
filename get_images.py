# imports for NBIA API calls

from tcia_utils import nbia
import pandas as pd
import requests
import json
import os
here = os.path.dirname(os.path.abspath(__file__))

# get list of available collections as JSON
respDict = nbia.getCollections()

# undo formatting
respList = []
for collection in respDict:
    respList += [collection["Collection"]]
print(json.dumps(respList, indent=2))

# response = requests.get('https://services.cancerimagingarchive.net/nbia-api/services/v1/getCollectionValues')
keepList = ["Mouse-Mammary"]

for collection in keepList:
    data = nbia.getSeries(collection=collection)#, modality="MR", manufacturer="SIEMENS")
    print(json.dumps(data[0], indent=2))
    #nbia.downloadSeries(data, number=3)
    nbia.downloadSeries(data, path = os.path.join(here, "tcia_downloads", collection))
