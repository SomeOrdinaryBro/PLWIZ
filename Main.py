import re
import subprocess
from urllib.parse import urlparse
from pytube import YouTube

def is_valid_url(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme in ['http', 'https'] and (parsed_url.netloc.endswith('youtube.com') or parsed_url.netloc.endswith('youtu.be'))

def audio_downloader():
    link = input("Paste your YouTube link here: ")

    if not is_valid_url(link):
        print("Invalid YouTube link.")
        return

    try:
        yt = YouTube(link)
    except Exception as e:
        print("An error occurred while processing the link.")
        print(e)
        return

    audio = yt.streams.filter(only_audio=True).first()
    if audio is None:
        print("No audio stream found for this video.")
        return

    audio_filename = re.sub(r'[^\w\s]+', '_', yt.title) + ".mp3"

    try:
        subprocess.run(["ffmpeg", "-i", audio.url, "-vn", "-c:a", "copy", audio_filename], check=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred while downloading the audio file.")
        print(e)
        return

    print(f"Audio '{audio_filename}' has been downloaded successfully.")

def video_downloader():
    url = input("Paste the YouTube video URL: ")

    if not is_valid_url(url):
        print("Invalid YouTube link.")
        return

    try:
        yt = YouTube(url)
    except Exception as e:
        print("An error occurred while processing the link.")
        print(e)
        return

    valid_qualities = ['360p', '480p', '720p', '1080p']
    quality = input("Enter the desired video quality (360p, 480p, 720p, or 1080p): ")
    if quality.lower() not in [q.lower() for q in valid_qualities]:
        print(f"Invalid quality. Available options are: {', '.join(valid_qualities)}")
        return

    video = yt.streams.filter(progressive=True, file_extension='mp4').get_by_resolution(quality)
    if video is None:
        print(f"No video stream found for quality '{quality}'.")
        return

    video_filename = re.sub(r'[^\w\s]+', '_', yt.title) + f" ({quality}).mp4"

    try:
        subprocess.run(["ffmpeg", "-i", video.url, "-c:v", "copy", "-c:a", "copy", video_filename], check=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred while downloading the video file.")
        print(e)
        return

    print(f"Video '{video_filename}' has been downloaded successfully.")

def main_menu():
    print("Select 1 for Video Downloader")
    print("Select 2 for Audio Downloader")
    print("Enter 'q' to quit")

    choice = input("Enter your choice: ")
    if choice == '1':
        video_downloader()
    elif choice == '2':
        audio_downloader()
    elif choice == 'q':
        return
    else:
        print("Invalid choice. Try again.")
        main_menu()

if __name__ == "__main__":
    main_menu()
