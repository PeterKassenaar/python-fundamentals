# some OS examples (directories, path). More info, for example:
# - https://realpython.com/working-with-files-in-python/#getting-a-directory-listing
# - https://www.programiz.com/python-programming/file-operation

# 0. Imports in this module
import os
from pathlib import Path

# 1. Getting a list of all files and (sub)directories in the current directory:
# print('All files in the current directory:: ')
# with os.scandir() as entries:
#     for entry in entries:
#         print(entry.name)

#2. Or, doing the same in the 'examples' directory, using pathlib:
# entries = Path('./examples')
# for entry in entries.iterdir():
#     print (entry)

# 3. Showing only files, and not (sub)directories
basePath = './examples'
subDirectories = []
print('Files in {0}'.format(basePath))
with os.scandir(basePath) as entries:
    for entry in entries:
        if entry.is_file():
            print('\t', entry.name)
        elif entry.is_dir():
            subDirectories.append(entry.name)

print('Subdirectories in {0}'.format(basePath))
for subdir in subDirectories:
    print('\t', subdir)
