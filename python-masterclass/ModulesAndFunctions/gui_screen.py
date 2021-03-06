import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry('640x480-8-200')

label = tkinter.Label(mainWindow, text='Tkiner Grid Demo')
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)


fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for number in range(1,30):
    fileList.insert(tkinter.END,number)

listScroll = tkinter.Scrollbar(mainWindow,orient=tkinter.VERTICAL,command=fileList.yview())
listScroll.grid(row=1,column=1,sticky='nsw',rowspan=2)
fileList['yscrollcommand']=listScroll.set

mainWindow.mainloop()
