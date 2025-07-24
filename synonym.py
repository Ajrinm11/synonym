from tkinter import *
from tkinter import ttk

root=Tk()

root.title("Synonym Dictionary")
root.geometry("500x460")
root.config(bg="darkseagreen")

title=Label(root, text="Synonym Dictionary",  font=("maple", 16), bg="darkseagreen",  fg="black")
title.pack(pady=15)
    
labl=Label(root, text="Enter a word",  font=("maple", 13), bg="darkseagreen",  fg="black")
labl.pack(pady=15)

entry = Entry(root, width=40)
entry.pack(pady=15)

dictionary={
    "happy":['delighted', 'joyful', 'elated'],
    "sad":['somber', 'dejected', 'upset'],
    "cold":['frigid', 'chilly', 'icy'],
    "hot":['scorching', 'warm', 'fiery'],
    "expensive":['lavish', 'costly', 'extravagant'],
    "cheap":['afforable', 'reasonable', 'economical'],
    "good":['excellent', 'wonderful', 'incredible'],
    "bad":['abysmal', 'terrible', 'horrible'],
    "strong":['tough', 'sturdy', 'hefty'],
    "weak":['flimsy', 'delicate', 'fragile']
    
    }

def find():
    word = entry.get().lower()  
    if word in dictionary:  
        synonyms = dictionary[word]  
        labl2.config(text=f"Synonyms: {', '.join(synonyms)}") 
    else: 
        labl2.config(text="Sorry, choose a different word.")  

def resetfunction():
    entry.delete(0, END) 
    labl2.config(text="")

lookup = Button(root, text="Find Synonyms!", command=find, font=("maple", 12), bg="pink",  fg="black")
lookup.pack(pady=15)

labl2=Label(root, text="",  font=("maple", 13), bg="darkseagreen",  fg="black")
labl2.pack(pady=15)

reset = Button(root, text="Reset", command=resetfunction, font=("maple", 12), bg="cadetblue",  fg="white")
reset.pack(pady=15)

root.mainloop()