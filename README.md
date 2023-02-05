# YouTube Audio/Video Downloader
A simple python script to download YouTube audio or video in a chosen quality. The script uses re, subprocess, urlparse from urllib.parse, and YouTube from pytube libraries.

# Requirements
**1. Python 3**  
* You can download the latest version of Python 3 from the official website.  
    * **(https://www.python.org/downloads/)**  
  
**2. ffmpeg**  

* On Windows: you can download the latest version of ffmpeg from the official website.  
    * **(https://ffmpeg.org/download.html)**  
  
* On macOS: you can use Homebrew to install ffmpeg. Run the following command in terminal:   
    * **brew install ffmpeg**  
  
* On Linux: you can use the package manager to install ffmpeg. For example, on Ubuntu you can run the following command:  
    * **sudo apt-get install ffmpeg**  
  
**3. pytube library**  
  
* You can use pip to install pytube by running the following command in terminal/command prompt:  
    * **pip install pytube3**  
  
  
# How to run ?
* Clone the repository  
* Run the script using the command 'python main.py'  
* Enter the YouTube link and choose whether you want to download audio or video.  
* Enter the desired quality (for video) or press Enter to use the default quality (for audio)  
* The downloaded audio/video will be in the current directory with a filename generated from the video title and desired quality.  

# Contributing
This project is open to contributions. Feel free to raise an issue or submit a pull request.
