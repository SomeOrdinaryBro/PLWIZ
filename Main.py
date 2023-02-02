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
    print("What Downloader would you like to use")
    print("-----------------------------------------------------")
    print(" ")
    print("Select 1 for Video Downloader")
    print("Select 2 for Audio Downloader")
    print(" ")
    print("videos will be downloaded in mp4 format & audios in mp3")
    print(" ")
    print("-----------------------------------------------------")  
    choice = input("Enter Your choice : ")

  
    if choice in ('1', '2'):
      
        if choice == '1':
            Video_Downloader()

        elif choice == '2':
            Audio_Downloader()

        next_calculation = input("Would you like to download another video/audio? (yes/no): ")
      
        if next_calculation.lower() != "yes":
            print("Exiting the program.")
            exit()
        else:
          print("Continuing the program.")
