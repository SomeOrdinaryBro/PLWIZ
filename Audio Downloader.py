from pytube import YouTube

link = input("Enter the YouTube video link: ")
yt = YouTube(link)

audio = yt.streams.filter(only_audio=True).first()

audio.download('./')

print("Audio downloaded successfully!")
