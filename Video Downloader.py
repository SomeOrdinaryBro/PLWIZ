from pytube import YouTube

link = input("Enter the YouTube video link: ")
yt = YouTube(link)

video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

video.download('./')

print("Video downloaded successfully!")
