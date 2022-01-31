import shutil
import os

def copyFile(filename, pathToCopyTo):
    os.makedirs(os.path.dirname(pathToCopyTo), exist_ok=True)
    shutil.copy(filename, pathToCopyTo)