from pytube import YouTube

def Audio_Downloader():

  link = input("Paste your YouTube link here: ")
  yt = YouTube(link)

  audio = yt.streams.filter(only_audio=True).first()
  audio.download('./')

  print("Audio Downloaded Successfully")

def Video_Downloader():
  def download_video(url, quality='360p'):
    
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').get_by_resolution(quality)
    video.download(filename=yt.title)
    print(f"Video '{yt.title}' with {quality} quality has been downloaded successfully.")
    
  url = input("Paste the YouTube video URL: ")
  quality = input("\n480p\n720p\n1080p\n\nNote: if the program breaks after you type in the quality, that means the video isnt available on that quality or you typed it wrong\n\nExample: 144p or 1080p\n\nEnter the desired video quality:  ")
  
  while True:
      download_video(url, quality)
      quality_choice = input("change the video quality? (y/n): ")
      if quality_choice.lower() == 'y':
          quality = input("Enter the desired video quality: ")
      else:
        Another_Video()

def Another_Video():
  next_calculation = input("Would you like to download another video or an audio? (y/n): ")
   
  if next_calculation.lower() != "y":
    print("Exiting the program.")
    exit()
  else:
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
