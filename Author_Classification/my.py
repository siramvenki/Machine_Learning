from os import listdir
import docx
import csv
from os.path import isfile,join

myPath = "DUMP"

def fileToText(fileName,roll):
    doc = docx.Document(join(myPath,roll,fileName))
    content=""
    for para in doc.paragraphs:
        content+=para.text.encode('UTF-8')+" "
    # content =" ".join(content.split())
    # content = content.lower()
    #     content = content.translate(None, string.punctuation)
    return content

# fileDict = {roll:[f for f in listdir(join(myPath,roll)) if isfile(join(myPath,roll,f))]for roll in listdir(myPath)}

# textDict = {roll:[fileToText(f,roll) for f in listdir(join(myPath,roll)) if isfile(join(myPath,roll,f))]for roll in listdir(myPath)}


for roll in listdir(myPath):
    temp=""
    for f in listdir(join(myPath,roll)):
        temp+=fileToText(f,roll)
        temp=temp.replace(",","")
        temp=" ".join(temp.split())
        print roll+","+temp