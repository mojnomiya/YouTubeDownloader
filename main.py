# importing modules
from pytube import YouTube
from tkinter import *

res = 0


def downloader():
    global res
    t = text.get()
    video = YouTube(t)

    if res1.get() == 18:
        res = 18
    elif res2.get() == 22:
        res = 22
    elif res3.get() == 137:
        res = 137

    video_streams = video.streams.get_by_itag(res)

    if video_streams:
        video_streams.download(filename="", output_path="/Users/mojnu/Downloads")
        Label(window, text="Downloaded Successfully").pack()
    else:
        Label(window, text="No stream found for the selected resolution").pack()


window = Tk()
text = StringVar(window, value="YouTube Url")

# Set the size of the tkinter window
window.geometry("700x350")
window.title("DTube")
Label(window, text="YOUTUBE VIDEO DOWNLOADER", bg='white', font='Calibre 15').pack()
Label(window, text="Enter the link to download", font='Calibre 12').pack()
Entry(window, textvariable=text, width=50).pack()  # entry field

res1 = IntVar(value=18)
res2 = IntVar(value=22)
res3 = IntVar(value=137)
Checkbutton(text='360p', variable=res1).pack()
Checkbutton(text='720p', variable=res2).pack()
Checkbutton(text='1080p', variable=res3).pack()

# creating a button
Button(window, text="Download", bg='green', command=downloader).pack()

window.mainloop()
