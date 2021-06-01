from array import *


# import tkinter
# import tkinter as tk
# # GUI
# from tkinter import *
#
# root = tk.Tk()
#
# frame = Frame(root)
# frame.pack()
#
# bottomFrame = Frame(root)
# bottomFrame.pack(padx=10, pady=10, side=BOTTOM)
#
# label = tk.Label(frame, text="Search Key")
# label.pack(side=LEFT)
#
# entry = tk.Entry(frame, bd=5)
# entry.pack(side=RIGHT)
#
# btn = tkinter.Button(bottomFrame, text="Perform Search")
#
# btn.pack()
#
# root.mainloop()

# GUI ends

def handleDoc1():
    doc1 = open('doc1.txt', 'r')
    readLineFromTxt = doc1.readlines()
    for line in readLineFromTxt:
        list = line.split()
        for word in list:
            if word not in tokensTable:
                tokensTable[word] = {}
                tokensTable[word][doc1Str] = 1
                tokensTable[word][doc2Str] = 0


def handleDoc2():
    doc2 = open('doc2.txt', 'r')
    readLineFromTxt2 = doc2.readlines()
    for line in readLineFromTxt2:
        list = line.split()
        for word in list:
            if word not in tokensTable:
                tokensTable[word] = {}
                tokensTable[word][doc1Str] = 0
                tokensTable[word][doc2Str] = 1
            if word in tokensTable:
                tokensTable[word][doc2Str] = 1


def handleList():
    for word in searchList:
        doc1value = tokensTable[word]['doc1']
        doc2value = tokensTable[word]['doc2']
        operatorList.append(int(str(doc1value) + str(doc2value)))


def handleAND(operation):
    res = [0, 0]
    val0 = operation[0] % 10
    operation[0] = operation[0] / 10
    val1 = operation[1] % 10
    operation[1] = operation[1] / 10
    if val1 and val0:
        res[0] = 1
    if operation[0] % 10 and operation[1] % 10:
        res[1] = 1
    return res


def handleOR(operation):
    print(operation)


def handleNOT(operation):
    print(operation)


tokensTable = {}
doc1Str = 'doc1'
doc2Str = 'doc2'
handleDoc1()
handleDoc2()
searchKey = str('software coding')
searchList = searchKey.split()
operatorList = []
handleList()
print(operatorList)
print(handleAND(operatorList))

