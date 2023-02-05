#PLWIZ

import re
import subprocess
from urllib.parse import urlparse
from pytube import YouTube

# This code imports the required libraries (re, subprocess, urlparse from urllib.parse, and YouTube from pytube).
# The function is_valid_url takes in a url and checks if it is a valid YouTube url. 
# The url is parsed using the urlparse method from the urllib.parse library. 
# The function returns True if the scheme of the url is either 'http' or 'https' and if the netloc of the url ends with 'youtube.com' or 'youtu.be', otherwise, it returns False.


# This function checks if the given url is a valid YouTube url
def is_valid_url(url):
    # Parsing the url and getting the different components like scheme, netloc, etc.
    parsed_url = urlparse(url)

    # Checking if the scheme of the url is either 'http' or 'https' and if the netloc of the url ends with 'youtube.com' or 'youtu.be'
    return parsed_url.scheme in ['http', 'https'] and (parsed_url.netloc.endswith('youtube.com') or parsed_url.netloc.endswith('youtu.be'))

def audio_downloader():
    # Get the link of the YouTube video from the user
    link = input("Paste your YouTube link here: ")

    # Check if the link is a valid YouTube link
    if not is_valid_url(link):
        print("Invalid YouTube link.")
        return

    try:
        # Use the YouTube class from the pytube library to extract information about the video
        yt = YouTube(link)
    except Exception as e:
        # If an exception occurs while processing the link, print the error message
        print("An error occurred while processing the link.")
        print(e)
        return

    # Filter the streams for audio-only and select the first audio stream
    audio = yt.streams.filter(only_audio=True).first()
    if audio is None:
        # If no audio stream is found, print an error message
        print("No audio stream found for this video.")
        return

    # Generate a filename for the audio by removing any special characters from the video title
    audio_filename = re.sub(r'[^\w\s]+', '_', yt.title) + ".mp3"

    try:
        # Use the subprocess module to run the ffmpeg command to download the audio stream
        subprocess.run(["ffmpeg", "-i", audio.url, "-vn", "-c:a", "copy", audio_filename], check=True)
    except subprocess.CalledProcessError as e:
        # If an error occurs while downloading the audio file, print the error message
        print("An error occurred while downloading the audio file.")
        print(e)
        return

    # Print a success message indicating that the audio file has been downloaded successfully
    print(f"Audio '{audio_filename}' has been downloaded successfully.")

def video_downloader():
    # Get the YouTube video link from the user
    url = input("Paste the YouTube video URL: ")

    # Check if the URL is a valid YouTube link
    if not is_valid_url(url):
        print("Invalid YouTube link.")
        return

    try:
        # Create a YouTube object using the pytube library to extract information about the video
        yt = YouTube(url)
    except Exception as e:
        # If an error occurs while processing the link, print the error message
        print("An error occurred while processing the link.")
        print(e)
        return

    # Define the available video quality options
    valid_qualities = ['360p', '480p', '720p', '1080p']

    # Get the desired video quality from the user
    quality = input("Enter the desired video quality (360p, 480p, 720p, or 1080p): ")

    # Check if the desired video quality is available
    if quality.lower() not in [q.lower() for q in valid_qualities]:
        print(f"Invalid quality. Available options are: {', '.join(valid_qualities)}")
        return

    # Get the video stream with the desired quality
    video = yt.streams.filter(progressive=True, file_extension='mp4').get_by_resolution(quality)
    if video is None:
        # If no video stream is found with the desired quality, print an error message
        print(f"No video stream found for quality '{quality}'.")
        return

    # Generate a filename for the video by removing any special characters from the video title and adding the quality
    video_filename = re.sub(r'[^\w\s]+', '_', yt.title) + f" ({quality}).mp4"

    try:
        # Use the subprocess module to run the ffmpeg command to download the video stream
        subprocess.run(["ffmpeg", "-i", video.url, "-c:v", "copy", "-c:a", "copy", video_filename], check=True)
    except subprocess.CalledProcessError as e:
        # If an error occurs while downloading the video file, print the error message
        print("An error occurred while downloading the video file.")
        print(e)
        return

    # Print a success message indicating that the video file has been downloaded successfully
    print(f"Video '{video_filename}' has been downloaded successfully.")

# This is the main menu where you get to choose what you want to do
# You can either download a video or an audio
def main_menu():

# This will print some options for you to choose from
    print("Select 1 for Video Downloader")
    print("Select 2 for Audio Downloader")
    print("Enter 'q' to quit")

    # You get to choose your option by typing 1, 2 or 'q'
    choice = input("Enter your choice: ")

    # If you choose 1, the video downloader will start
    if choice == '1':
        video_downloader()
    # If you choose 2, the audio downloader will start
    elif choice == '2':
        audio_downloader()
    # If you choose 'q', the program will quit
    elif choice == 'q':
        return
    # If you choose anything else, the program will ask you to try again
    else:
        print("Invalid choice. Try again.")
        main_menu()

# This makes sure the main_menu is run only if this script is run directly
# and not imported as a module
if __name__ == "__main__":
    main_menu()
