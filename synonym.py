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
#this dictionary (some) has been generated by GPT :D
dictionary = {
    "happy": ['delighted', 'joyful', 'elated'],
    "sad": ['somber', 'dejected', 'upset'],
    "cold": ['frigid', 'chilly', 'icy'],
    "hot": ['scorching', 'warm', 'fiery'],
    "expensive": ['lavish', 'costly', 'extravagant'],
    "cheap": ['affordable', 'reasonable', 'economical'],
    "good": ['excellent', 'wonderful', 'incredible'],
    "bad": ['abysmal', 'terrible', 'horrible'],
    "strong": ['tough', 'sturdy', 'hefty'],
    "weak": ['flimsy', 'delicate', 'fragile'],
    "fast": ['quick', 'swift', 'speedy'],
    "slow": ['lethargic', 'sluggish', 'unhurried'],
    "smart": ['intelligent', 'bright', 'clever'],
    "dumb": ['unintelligent', 'dimwitted', 'foolish'],
    "big": ['large', 'huge', 'enormous'],
    "small": ['tiny', 'petite', 'minuscule'],
    "beautiful": ['gorgeous', 'stunning', 'lovely'],
    "ugly": ['unattractive', 'hideous', 'unsightly'],
    "loud": ['noisy', 'boisterous', 'deafening'],
    "quiet": ['silent', 'hushed', 'soft'],
    "rich": ['wealthy', 'affluent', 'prosperous'],
    "poor": ['needy', 'destitute', 'impoverished'],
    "clean": ['spotless', 'immaculate', 'tidy'],
    "dirty": ['filthy', 'grimy', 'unclean'],
    "funny": ['amusing', 'hilarious', 'witty'],
    "boring": ['dull', 'tedious', 'monotonous'],
    "friendly": ['amiable', 'cordial', 'welcoming'],
    "mean": ['cruel', 'rude', 'spiteful'],
    "bright": ['luminous', 'radiant', 'vivid'],
    "dark": ['dim', 'gloomy', 'shadowy'],
    "easy": ['simple', 'effortless', 'straightforward'],
    "hard": ['difficult', 'challenging', 'tough'],
    "tired": ['exhausted', 'weary', 'fatigued'],
    "energetic": ['lively', 'active', 'vigorous'],
    "angry": ['mad', 'furious', 'irate'],
    "calm": ['peaceful', 'tranquil', 'serene'],
    "honest": ['truthful', 'sincere', 'upright'],
    "dishonest": ['deceitful', 'untruthful', 'fraudulent'],
    "old": ['ancient', 'elderly', 'aged'],
    "young": ['youthful', 'juvenile', 'fresh'],
    "lazy": ['idle', 'sluggish', 'inactive'],
    "hardworking": ['diligent', 'industrious', 'dedicated'],
    "fat": ['chubby', 'plump', 'overweight'],
    "thin": ['slim', 'lean', 'skinny'],
    "nice": ['pleasant', 'kind', 'agreeable'],
    "rude": ['impolite', 'disrespectful', 'abrasive'],

    # Coding/Programming terms
    "bug": ['error', 'glitch', 'issue'],
    "fix": ['patch', 'resolve', 'correct'],
    "code": ['script', 'program', 'source'],
    "debug": ['troubleshoot', 'analyze', 'test'],
    "function": ['method', 'procedure', 'routine'],
    "variable": ['identifier', 'name', 'symbol'],
    "loop": ['iteration', 'cycle', 'repeat'],
    "crash": ['fail', 'halt', 'break'],
    "compile": ['build', 'translate', 'assemble'],
    "deploy": ['launch', 'release', 'publish'],
    "optimize": ['improve', 'enhance', 'refactor'],
    "database": ['data store', 'repository', 'storage']
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
