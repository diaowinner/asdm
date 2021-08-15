# Import
import requests
import os

print('''
 _______  _______  ______   __   __ 
|   _   ||       ||      | |  |_|  |
|  |_|  ||  _____||  _    ||       |
|       || |_____ | | |   ||       |
|       ||_____  || |_|   ||       |
|   _   | _____| ||       || ||_|| |
|__| |__||_______||______| |_|   |_|
     Auto Scratch-Desktop Mirror
           DOWNLOAD START

''')

# Create 'output'
if not os.path.exists('output'):
    os.mkdir('output')

# Download 'Scratch Setup.exe' for Windows
r = requests.get('https://www.cns11643.gov.tw/AIDB/Open_Data.zip', stream=True)

with open(r'./output/Open_Data.zip', "wb") as f:
    for chunk in r.iter_content(chunk_size=512):
        f.write(chunk)

print('Download scratch-desktop for windows done.')

# Get Scratch Version

fl = open("scratch-version","w+")
fl.write("")
version = str(int(time.time()))
fl.write()
fl.close()
print('Get version done. version :', version, '. Cost',getVersion.elapsed.total_seconds(),'sec.')
