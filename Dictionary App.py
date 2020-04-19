import json
from difflib import *
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from functools import partial




def open_files():
    data=json.load(open("data.json","r"))
    file=open("history.txt","a+")
    return data

def clear_fields():
    result_box.delete('1.0',END)
    search_box.delete('0',END)

def working_part(search_word):
    data=open_files()
    while True:
        word=search_word.get()
        if not word:
           break
        word=word.lower()
        history(word)
        if word not in data:
            suggest_word=(get_close_matches(word,data.keys(),cutoff=0.7))[0]
            ch=messagebox.askyesno("Suggestion ",suggest_word,icon='question')
                
            if ch:
                meaning(suggest_word)
                break
            else:
                ch1=messagebox.askyesno("Word doesn't exists","Wrong word. Want to search again?",icon='error')
                if ch1:
                    clear_fields()
                    break
        else:
            meaning(word)
            break



def history(word):              
        word=word
        file=open("history.txt","a+")
        file.write(word)
        file.write("\n")
        file.close()

    
def meaning(word):
        data=open_files()
        meaning=data[word]
        for each_word in meaning:
            result_box.insert(END,each_word+'\n\n')
        





window=Tk(className="Dictionary")
window.iconbitmap(default='icon.ico')   
messagebox.showinfo("Description","Search meaning of any word using this Dictionary Application")

window.geometry("400x300")
window.resizable(0,0)


myfont=Font(family="Times",size=15)

lable_one=Label(window,text="Enter the word to search",font=myfont)
lable_one.grid(row=2,column=3,columnspan=4,padx=1,pady=1)

lable_two=Label(window,text="Dictionary Application",font=("Helvetica",20,"bold"))
lable_two.grid(row=0,column=2,columnspan=6,pady=5)

search_word=StringVar()
search_box=Entry(window,textvariable=search_word,relief=SUNKEN)
search_box.grid(row=3,column=3,columnspan=4,pady=5)
search_box.focus_set()


search_btn= Button(window,text="Search",command=partial(working_part,search_word),cursor='hand2')    
search_btn.grid(row=5,column=3,columnspan=3,padx=5,pady=5)


clear_btn= Button(window,text="Clear",command=clear_fields)    
clear_btn.grid(row=5,column=4,columnspan=3,padx=5,pady=5)

result_box=Text(window,height=20,width=50,wrap="word")
result_box.grid(row=7,column=2,rowspan=6,columnspan=6,padx=2,pady=2)


window.mainloop()


















     

    
    
    
