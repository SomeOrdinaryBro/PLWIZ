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

while True:
    print("What Service would you like to use")
    print("-----------------------------------------------------")
    print(" ")
    print("Select 1 -  Video Downloader")
    print("Select 2 -  Audio Downloader") 
    print("-----------------------------------------------------")  
    choice = input("Enter Your choice : ")

  
    if choice in ('1', '2'):
      
        if choice == '1':
            SalarayKal()

        elif choice == '2':
            ShapesKal()

        next_calculation = input("Would you like to download another video/audio? (YES/NO): ")
        if next_calculation == "NO":
            break
        if next_calculation == "No":
            break
        if next_calculation == "nO":
            break
        if next_calculation == "No":
            break