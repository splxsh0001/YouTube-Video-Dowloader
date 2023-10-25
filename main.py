import tkinter
import customtkinter
from pytube import YouTube
import os


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progess)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishlabel.configure(text="")

        video.download()
        finishlabel.configure(text="Dowloaded!", text_color ="green")
    except:
        finishlabel.configure(text="Video Failed to Dowload!", text_color="red")

def startmp3():
    try:
        ytlink = link.get()
        ytONjet = YouTube(ytlink, on_progress_callback=on_progess)
        video = ytONjet.streams.filter(only_audio=True).first().download()
        new_name = os.path.splitext(video)
        os.rename(video, new_name[0]+ ".mp3")
        
        title.configure(text=ytONjet.title, text_color="white")
        finishlabel.configure(text="")

        video.download()
        finishlabel.configure(text="Dowloaded!", text_color ="green")
    except:
        finishlabel.configure(text="Video Failed to Dowload!", text_color="red")



def on_progess(stream, chunk ,bytes_remaining):
    total_size = stream.filesize
    bytes_dowloaded = total_size - bytes_remaining

    percentage_of_completion = bytes_dowloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    # Update progess
    progessbar.set(float(percentage_of_completion ) / 100)
    
#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#fframe
app = customtkinter.CTk()
app.geometry("720x480")
app.title("youtube Downloader by Splxsh!")

#uui
title = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10, pady=10)


#link
url_var = tkinter.StringVar()
link =customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#finished
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

#progess percerntage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progessbar = customtkinter.CTkProgressBar(app, width=400)
progessbar.set(0)
progessbar.pack(padx=10, pady=10)

#download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

mp3 = customtkinter.CTkButton(app, text="Mp3", command=startmp3)
mp3.pack(padx=10, pady=10)

#watermark
watermark = customtkinter.CTkLabel(app, text="Made By Splxsh", text_color="blue")
watermark.pack(padx=20, pady=100)

#run app
app.mainloop()