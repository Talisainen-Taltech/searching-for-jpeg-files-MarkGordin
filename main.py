import os
import requests
import zipfile

for i in range(10,200):
    filename = "file%d" %i
    f = open('random_files/'+filename, 'rb').read(3)
    print(f)
    if f == (b'\xff\xd8\xff'):
        print('jpeg found')
        os.rename('random_files/' + filename, 'random_files/' + filename + ".jpg")
    else: os.remove('random_files/' + filename)