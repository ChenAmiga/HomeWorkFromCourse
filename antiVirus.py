import os
import requests
import time

virusTotalApiUploadUrl= "https://www.virustotal.com/api/v3/files"
myApiKey="15c1242e49e00039c94dadc6232db0b8417f9dcee60c164693dccbd27d2a9d91"
headers = {
    "accept": "application/json",
    "x-apikey": myApiKey,
    }

# check if its another folder or if its a file
def iterate_file(folder_path):
 for fileName in os.listdir(folder_path):
   fullPath=os.path.join(folder_path,fileName)
   if os.path.isdir(fullPath):
     iterate_file(fullPath)
   else:
        scan_file(fullPath,fileName)
 

# send it for scaning
def send(fullPath):
   files= {"file": open(fullPath,"rb")}
   response = requests.post(virusTotalApiUploadUrl, headers=headers, files=files)
   return(response.json()["data"]["id"])

#scan and wait for respond
def scan_file(file_path, fileName):
     virusTotalApiReportUrlForEachFile= "https://www.virustotal.com/api/v3/files/"+send(file_path)
     response= requests.get(virusTotalApiReportUrlForEachFile, headers=headers)
     response=response.json()
     if response["data"]["attributes"]["status"]=="completed":
        if response["data"]["attributes"]["stats"]["malicious"]>0:
           print (fileName, " have virus")
        else:
           print(fileName, " is fine")
     else:
        print ("waiting for respond")
        time.sleep(5)
        scan_file(file_path,fileName)


iterate_file(folder_path=r"C:\Users\alona\Downloads\anti virus")