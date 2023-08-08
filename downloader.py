from pytube import YouTube
from sys import argv

print("Enter video link: ")
link = input()
yt = YouTube(link)

yd = yt.streams.get_highest_resolution()
yd.download("YoutubeVideoDownloader\downloads") ## enter your file path