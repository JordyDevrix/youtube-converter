from pytube import YouTube
import os

url = "https://youtu.be/olPZE4K2rC0"
video = YouTube(url)
print("Title:", video.title)
print("downloading...")
out_path = video.streams.filter(only_audio=True).first().download()
new_name = os.path.splitext(f"C:/Users/2109j/Downloads/{video.title}.mp3")
print(new_name)
print("done")
