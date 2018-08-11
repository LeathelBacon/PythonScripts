'''
Author: Oriel Bacdner
Date: 11/08/18

Description:
This script downloads the tar file from the requested URL, unpacks it and execute the docker compose file and command
Note: after cloning the repo place the script and docker-compose.yml inside the cloned dir
'''

#!/usr/bin/python
import urllib
import tarfile
import os
import requests
import json
import sys
import time

#Downloading and extracting the files locally
downloadFile = urllib.URLopener()
downloadFile.retrieve("https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz", "file.tar.gz")
tar= tarfile.open("file.tar.gz")
os.system("mkdir images")
tar.extractall("./public/images")
tar.close()

#The step to launch the docker-compose up (added the -d to detach or else script will not continue)
os.system("docker-compose up -d")

print 'File downloaded and extracted!!! "\n'

#Need to wait a few seconds before making the health check to give time for the containers to be fully up
time.sleep(10)

#Below is the healthcheck
response = requests.get('http://localhost:3000/health')
data = response.json()
if data[u'isSuccessful'] == True:
        print 'Health check is all good and running!'
else:
        print 'Internal 500 error, aborting script!'
        sys.exit()






