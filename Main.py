def Audio_Downloader():
  from pytube import YouTube

  link = input("Paste your YouTube link here: ")
  yt = YouTube(link)

  audio = yt.streams.filter(only_audio=True).first()
  audio.download('./')

  print("Audio Downloaded Successfully")

def Video_Downloader():
  from pytube import YouTube
  
  link = input("Enter the YouTube video link: ")
  yt = YouTube(link)
  
  video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
  
  video.download('./')
  
  print("Video downloaded successfully!")

