#TheWhistler

from parser import Parser
from mover import *
import pdb

dst = "/home/thewhistler/Projects/playground/"

par = Parser("files.nav")

takeBackup("t1", par.content)

#for i in par.content:
#    for k in i[1]:
#        t = i[0].split("/")
#        fdst = dst + t[-2] + "/" + k
#        copyFile(i[0] + k, fdst)