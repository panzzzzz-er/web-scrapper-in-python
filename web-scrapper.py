from cProfile import label
from tkinter import *
import requests
from bs4 import BeautifulSoup as bs


def printInput():
    github_user = entry_1.get()
    #github_user = input('Input Github User: ')
    url = 'https://github.com/' + github_user
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    profile_image = soup.find('img', {'alt': 'Avatar'})['src']
    print(profile_image)
    lbl.config(text="Provided Input: "+github_user)
    lb2.config(text=""+profile_image)


root = Tk()  # creates the frame for the tkinter window
root.geometry('500x500')
root.title("WebScrapper in Python")

label_0 = Label(root, text="Form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Username", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root)
entry_1.place(x=240, y=130)

Button(root, text='Submit', width=20, bg='brown',
       fg='white', command=printInput).place(x=160, y=260)

lbl = Label(root, text="")
lbl.place(x=130, y=300)

lb2 = Label(root, text="")
lb2.place(x=130, y=350)

root.mainloop()
print("FORM CREATED SUCCESSFULLY")
