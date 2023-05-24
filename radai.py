from tcia_utils import nbia
import pandas as pd
import requests
import json
import logging

# Check current handlers
# print(logging.root.handlers)

# Remove all handlers associated with the root logger object.
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
# print(logging.root.handlers)

# Set handler with level = info
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", level=logging.INFO)

print("Logging set to INFO")

# get list of available collections as JSON
collections = nbia.getCollections()
# print(json.dumps(collections, indent=2))

data = nbia.getSeries(collection="Soft-tissue-Sarcoma")
print(json.dumps(data, indent=2))

seriesUid = "1.3.6.1.4.1.14519.5.2.1.5168.1900.104193299251798317056218297018"
# nbia.viewSeries(seriesUid = seriesUid)

# getSeries with query parameters
data = nbia.getSeries(collection="TCGA-BRCA", modality="MR", manufacturer="SIEMENS")

print(len(data), "Series returned")
