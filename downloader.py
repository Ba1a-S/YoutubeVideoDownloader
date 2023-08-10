from pytube import YouTube
import tkinter as tk
from tkinter import simpledialog
 
window = tk.Tk()
promptText = tk.Label(
    text="Enter Youtube Address Below",
    foreground="white",  
    background="gray",
    width=25,
    height=10
)
entry = tk.Entry()
button = tk.Button(
    text="Convert Link to MP4",
    width=25,
    height=3,
    bg="blue",
    fg="yellow",
)

def click(event):
    print("The button was clicked!")
    link = entry.get()
    window.quit()
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.download("YoutubeVideoDownloader\downloads") ## enter your file path


button.bind("<Button-1>", click)

promptText.pack()
entry.pack()
button.pack()
window.mainloop()

