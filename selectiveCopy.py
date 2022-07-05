import os, re, shutil
from pathlib import Path
# Line 35 commented out to prevent repeat copy

# create a regex to find the .py extension
regex = re.compile(r'py$')

# Choose the folder to copy
folder = os.path.abspath('/Users/Lucas/Python/')

# Create the new python folder
newPythonFolder = Path('/Users/Lucas/Python/New Python Folder')

if newPythonFolder.exists():
	pass
else:
	os.makedirs('/Users/Lucas/Python/New Python Folder')

# Walk through a folder tree
for foldername, subfolders, filenames in os.walk(folder):
	for filename in filenames:

		# Find the .py files with the 'folder'
		pyRegex = regex.findall(filename)
		if not pyRegex:
			continue  # Skip the files which don't have .py

		pythonFile = os.path.basename(filename)

		# Get the full filepath
		fullPath = foldername + '/' + pythonFile
		print(fullPath)

		print(f'Copying .py file "{pythonFile}" in "{foldername}/..." to "{newPythonFolder}/..."')
		# shutil.copy(fullPath, newPythonFolder) # Commented out to prevent repeat copy

print('Done.')
