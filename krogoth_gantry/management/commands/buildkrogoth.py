import os

files = os.listdir('static/web/core/')
for file in files:
    arr = file.split('.')
    print('- - - - - - - - - - - ' + str(len(arr)))
    print(arr[0])
    print(arr[len(arr) - 2])
    print(arr[len(arr) - 1])


