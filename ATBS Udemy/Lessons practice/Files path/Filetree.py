import os
print(os.getcwd())

for foldername, subfolder, files in os.walk('d:\\Py'):
    print('The folder is ' + foldername)
    print('The subfolder in the ' + (foldername) + ' is ' + str(subfolder))
    print('The files in the ' + (foldername) + ' is ' + str(files))
