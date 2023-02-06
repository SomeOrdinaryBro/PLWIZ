import pytube 

def download_video():
    # Prompt user to enter the link of the video they want to download
    link = input("Enter the link of the video you want to download: ")

    # Create a YouTube object and set the video link
    video = pytube.YouTube(link)

    # Stream the video with the highest resolution
    video_stream = video.streams.get_highest_resolution()

    # Download the video
    video_stream.download()

# Call the function to start the video downloader
download_video()


#this is a simple version of the PLWIZ.py that just downloads the video without checking the link or anything.
# you wont be able to choose video quality and what not.. i just a stripped down version of the code PLWIZ.py
