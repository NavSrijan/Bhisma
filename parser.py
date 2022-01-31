'''
# ~/.config/polybar/
!config
$
# ~/
!
$
'''
class Parser():
    def __init__(self, filename):
        try:
            self.file = open(filename, "r")
        except:
            raise Exception("File not found. Please check your path")
        self.content = [] #list Structure: [["Path to folder", [filenaname]]]
        self.parse()
    def parse(self):
        reader = self.file.readlines()
        reader = [i.strip("\n") for i in reader]
        temp2 = []
        for i in reader:
            if i[0]=="#":
                temp = i[1:]
            elif i[0]=="!":
                temp2.append(i[1:])
            elif i=="$":
                self.content.append([temp, temp2])
                temp2 = []
    def printHierarchy(self):
        for i in self.content:
            print(i[0])
            for k in i[1]:
                print(" "*7 + k)



#p = Parser("par.par")
#p.printHierarchy()
#print(p.content)