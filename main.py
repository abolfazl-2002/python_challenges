# get a filename and give the extension of that

fileFullName = input("filename:\n") # file name whit extention

# solution 1 
import os
def showExtention_1(filename):
    fileNameList= os.path.splitext(filename) # convert file name to list

    fileName = fileNameList[0] # file base name
    fileExtention = fileNameList[1] # file extention

    return """
    filename : {}
    fileextention : {}
    """.format(fileName,fileExtention)


# solution 2
def showExtention_2(filename):
    fileNameList = filename.rsplit(".",1) # convert file name to list

    fileName = fileNameList[0] # file base name
    fileExtention = fileNameList[1] # file extention

    return """
    filename : {}
    fileextention : .{}
    """.format(fileName,fileExtention)

# print(showExtention_1(fileFullName))
print(showExtention_2(fileFullName))
