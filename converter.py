from pytube import YouTube
from tkinter import *
import os

root = Tk()
root.geometry("300x200")
root.title("youtube converter")

main_frame = Frame(root, bg="grey")
main_frame.pack(padx=5, pady=5, fill="both", expand=True)

entry_widget = Entry(main_frame, font="Roboto, 15")
entry_widget.pack(fill="both", pady=50, padx=10)


def download_link(url):
    video = YouTube(url)
    out_path = video.streams.filter(only_audio=True).first().download()
    new_name = os.path.splitext(out_path)
    os.rename(out_path, new_name[0] + ".mp3")


convert_button = Button(main_frame,
                        font="Roboto, 15",
                        text="convert and download",
                        command=lambda: download_link(entry_widget.get()))
convert_button.pack(pady=0)

root.mainloop()
