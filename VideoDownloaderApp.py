import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import IntVar
from tkinter import OptionMenu
from tkinter import Checkbutton
from pytube import YouTube

def download_video_audio():
    video_url = url_entry.get()
    video_quality = quality_var.get() or '480p'
    download_video = video_var.get()
    download_audio = audio_var.get()
    if not video_url:
        messagebox.showerror("Error", "Please enter a valid YouTube video URL.")
        return
    yt = YouTube(video_url)
    if download_video:
        video = yt.streams.filter(progressive=True, file_extension='mp4').get_by_resolution(video_quality)
        file_name = filedialog.asksaveasfilename(defaultextension=".mp4", initialfile=yt.title, title="Save as")
        if file_name:
            video.download(file_name)
            messagebox.showinfo("Download Complete", "Video '{}' has been downloaded successfully.".format(yt.title))
    if download_audio:
        audio = yt.streams.filter(only_audio=True).get_by_resolution(video_quality)
        file_name = filedialog.asksaveasfilename(defaultextension=".mp3", initialfile=yt.title, title="Save as")
        if file_name:
            audio.download(file_name)
            messagebox.showinfo("Download Complete", "Audio '{}' has been downloaded successfully.".format(yt.title))

app = tk.Tk()
app.title("YouTube Downloader")
app.geometry("400x300")

url_label = tk.Label(app, text="YouTube Video Link:")
url_label.pack()

url_entry = tk.Entry(app)
url_entry.pack()

quality_var = tk.StringVar()
quality_var.set("480p")
quality_label = tk.Label(app, text="Quality:")
quality_label.pack()

quality_options = OptionMenu(app, quality_var, "360p", "480p", "720p", "1080p")
quality_options.pack()

video_var = IntVar()
video_download_check = Checkbutton(app, text="Download Video", variable=video_var, onvalue=1, offvalue=0)
video_download_check.pack()

audio_var = IntVar()
audio_download_check = Checkbutton(app, text="Download Audio", variable=audio_var, onvalue=1, offvalue=0)
audio_download_check.pack()

download_button = tk.Button(app, text="Download", command=download_video_audio)
download_button.pack()

app.mainloop()
