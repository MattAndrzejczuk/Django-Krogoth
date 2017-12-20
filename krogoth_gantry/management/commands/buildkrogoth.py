import os

files = os.listdir('krogoth_core/AKThemes/Pro/')
for file in files:
    arr = file.split('.')
    print('- - - - - - - - - - - ' + str(len(arr)))
    print(arr[0])
    print(arr[len(arr) - 2])
    print(arr[len(arr) - 1])


