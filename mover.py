import shutil
import os
import pdb
from zipfile import ZipFile

def copyFile(filename, pathToCopyTo):
    os.makedirs(os.path.dirname(pathToCopyTo), exist_ok=True)
    shutil.copy(filename, pathToCopyTo)
def takeBackup(backupName, pathList):
    try:
        os.mkdir("temp")
    except:
        pass
    backupName = "temp/"+backupName
    os.mkdir(backupName)
    dst = backupName + "/"
    for i in pathList:
        for k in i[1]:
            t = i[0].split("/")
            fdst = dst + t[-2] + "/" + k
            copyFile(i[0] + k, fdst)
    createZIP(backupName, backupName)
def getFilePaths(dirname):
    paths = []
    for root, directories, files in os.walk(dirname):
        for filename in files:
            filepath = os.path.join(root, filename)
            paths.append(filepath)
    return paths
def createZIP(filename, directoryToZip):
    pdb.set_trace()
    filePaths = getFilePaths(directoryToZip)
    with ZipFile(filename+".zip", 'w') as zip:
        for file in filePaths:
            zip.write(file)
    shutil.rmtree(directoryToZip)