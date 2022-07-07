from cProfile import label
from logging import exception
from tkinter import *
from tkinter import font
from matplotlib.pyplot import text
from pytube import YouTube
import os

# download function 
def download(link): 
    try:
        YouTube(link).streams.first().download("youtube_videos") # download the video witch is in link
        #initialize status pop-up window 
        p = Tk()
        p.title("status")
        p.resizable(False,False)
        p.geometry("200x100")
        p.grid_columnconfigure(0, weight=1)
        p.grid_rowconfigure((0,1), weight=1)
        msg = StringVar()
        msg.set("done")
        label = Label(p, text=msg.get())
        label.grid(row=0, column=0)
        button = Button(p, text="OK", command=p.destroy)
        button.grid(row=1, column=0)
        p.mainloop()
    except: # If there's an invalid link or empty link, show an error message
        error = Tk()
        error.title("Error")
        error.resizable(False, False)
        error.geometry("300x100")
        error.grid_rowconfigure((0,1), weight=1)
        error.grid_columnconfigure(0, weight=1)
        error_label = Label(error, text="Please enter a valid YouTube link")
        error_label.grid(row=0, column=0)
        button = Button(error, text="OK", command=error.destroy)
        button.grid(row=1, column=0)
        error.mainloop()



if "youtube_videos" not in os.listdir(os.getcwd()): #check if youtube_videos folder exist or not 
    #if the folder does not exist make folder
    os.mkdir("youtube_videos")


#stat of the GUI and the app 
app = Tk()
app.title("Youtube videos downloader developed by arshamX")
app.grid_rowconfigure((0,1),weight=1)
app.grid_columnconfigure((0,1),weight=1)
app.geometry("370x160")
app.resizable(False, False)
Label(app,text="video link : ").grid(row=0,column=0)
inputbox = Entry(app)
inputbox.grid(row=0,column=1)
Button(app,text="Download",command= lambda *args:download(inputbox.get())).grid(row=1,column=0,columnspan=2)
app.mainloop()



