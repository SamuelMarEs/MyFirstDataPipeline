#!/bin/bash
# Activate the python enviornment
source env/Scripts/activate
# Download the data sets from kaggle
bash DownloadDataSets.sh
# Load the data into a data base
# JOIN the tables and export the result as a .csv
python LoadData.py
# Deactivate the enviornment
deactivate
