from cProfile import label
from email.mime import image
from logging import root
import shutil
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import *
from pytube import YouTube
from PIL import Image, ImageTk

#function
def select_path():
    #allowuserto select path from directory
    path= filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    get_link = link_field.get()
    user_path= path_label.cget("text")
    screen.title('Downloading.....')
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()   

#movefile to selecteddirectory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another file...')


screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas( screen, width=500, height=500, bg='orange') 
canvas.pack()

#imageonProgramme
# image = Image.open("DHEERAJ MURMU (1).png")
#photo = ImageTk.PhotoImage(image)

#canvas.create_image(250,80, image=photo)



#linkfeild
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download Link", font=('Ariel', 15))

#selectpathfordownloading
path_label = Label(screen, text="Select path for Download", font=('Arial' , 15))
select_btn = Button(screen, text="Select", command=select_path)

#AddToWindow
canvas.create_window(250,280, window=path_label)
canvas.create_window(250,330, window=select_btn)



#addwidget
canvas.create_window(250,170, window=link_label)
canvas.create_window(250,220, window=link_field)

#downloadButton
download_btn = Button(screen, text="Download File",command=download_file)

#addtocanvas
canvas.create_window(250,390, window=download_btn)






screen.mainloop()
input()