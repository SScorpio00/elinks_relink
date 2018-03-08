#!/usr/bin/python
import sys
import fileinput

#Confirm Input
if len(sys.argv) != 2:
    print "Usage: elinks_relink.py <filename>"
    sys.exit()

fileName = sys.argv[1]
fileContent = ""
foundLinks = False
didSomething = False

#Loop line by line
for line in fileinput.input(fileName):
    #Parse the link and do a replace
    if foundLinks == True and line.find("."):
        linkNum = line[:line.find(".")].strip()
        url = line[line.find(".") + 1:].strip()
        fileContent = fileContent.replace("[" + linkNum + "]", "<a href='" + url + "'>[" + linkNum + "]</a>")
        didSomething = True

    #We've reached the link section
    if foundLinks == False and line.strip() == "References":
        foundLinks = True

    #Haven't reached the link section, so add line to buffer
    if foundLinks == False:
        fileContent += line

#Only modify the file if we changed any links
if didSomething == True:
    with open(fileName, "w") as outFile:
        outFile.write(fileContent)
