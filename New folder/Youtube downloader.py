#import libraries
from tkinter import *
from pytube import YouTube

#create the api windows or frame
root=Tk()
root.geometry("600x350")
root.resizable(0,0)
root.config(bg="lightblue")
root.title("Youtube video Downloader App")

#create the text and link entry widgets
Label(root,text="Download any youtube videos for free",font='arial 14 bold').place(x=100,y=20)
Label(root,text="Paste your link here",font='arial 14 ',bg="lightblue",fg="black").place(x=180,y=55)

#Entry widgets
videoLink=StringVar()
Entry(root,width=80,textvariable=videoLink).place(x=35,y=85)

#create the download funtion
def downloadVideo():
    url=YouTube(str(videoLink.get()))
    videoStream=url.streams.first()
    videoStream.download("C:\\Users\\murugan\\Desktop\\video")
    Label(root,text="Download Completed Successfully",font='Arial 14 bold',bg='white',fg='black').place(x=240,y=200)
#create a download button
Button(root,text="Download Now",font='Arial 16 bold',bg='white',padx=2,command=downloadVideo).place(x=180,y=120)

root.mainloop()