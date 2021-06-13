from bs4 import BeautifulSoup
from tkinter import *
from urllib import request

root = Tk()
root.geometry("650x450")
root.resizable(False, False)
root.title("Boogle Chrom")

icon = PhotoImage(file = "Boogle Chrom.png")
root.iconphoto(False, icon)

searchBar = Entry(root, width=60)
searchButton = Button(root, text="Go!", command=lambda: go())
content = Text(root)
content.config(state=DISABLED)

searchBar.grid(row=1, column=0)
searchButton.grid(row=2, column=0)
content.grid(row=0, column=0)

def go():
    url = request.urlopen(searchBar.get())
    rawData = url.read()

    soupData = BeautifulSoup(rawData, features="lxml")
    text = soupData.get_text()

    content.config(state=NORMAL)
    content.delete('1.0', END)
    content.insert(END, text)
    content.config(state=DISABLED)

root.mainloop()
