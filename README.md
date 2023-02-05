# YouTube Audio/Video Downloader
## Overview
This code is a script for downloading YouTube videos and audio in Python using the pytube library and ffmpeg command line tool. The script provides two main functions: audio_downloader and video_downloader. The audio_downloader function downloads the audio of a given YouTube video and saves it as an MP3 file, while the video_downloader function downloads the video and saves it as an MP4 file. The script also includes the is_valid_url function, which checks if a given URL is a valid YouTube URL.

## Requirements
1. [Python](https://www.python.org/) 3.x (Latest)
2. [pytube](https://github.com/nficano/pytube) library
3. [ffmpeg](https://www.ffmpeg.org/) command line tool

## Usage
To use the script, you need to install the required libraries and tools. The pytube library can be installed using the following command:

`pip install pytube`

The ffmpeg command line tool can be installed using the package manager of your operating system.

Once you have installed the required libraries and tools, you can run the script using the following command:

`python plwiz.py`

## Functions
### is_valid_url
This function takes a URL as an argument and returns **True** if the URL is a valid YouTube URL, and **False** otherwise. A YouTube URL is considered valid if it has a scheme of **'http'** or **'https'** and a **netloc** that ends with **'youtube.com'** or **'youtu.be'**.

### audio_downloader
This function allows the user to download the audio of a YouTube video. The user is prompted to enter the URL of the YouTube video, and the function checks if the URL is valid using the **is_valid_url** function. If the URL is valid, the function uses the **pytube **library to extract information about the video and download the first audio stream as an MP3 file. The name of the MP3 file is generated by removing special characters from the video title.

### video_downloader
This function allows the user to download a YouTube video. The user is prompted to enter the URL of the YouTube video and the desired quality of the video (360p, 480p, 720p, or 1080p). The function checks if the URL is valid using the **is_valid_url** function and if the desired quality is available. If the URL is valid and the desired quality is available, the function uses the **pytube **library to extract information about the video and download the video stream with the desired quality as an MP4 file. The name of the MP4 file is generated by removing special characters from the video title and appending the quality.

  
## How to run ?
* Clone the repository  
* Run the script using the command 'python main.py'  
* Enter the YouTube link and choose whether you want to download audio or video.  
* Enter the desired quality (for video) or press Enter to use the default quality (for audio)  
* The downloaded audio/video will be in the current directory with a filename generated from the video title and desired quality.  

## Contributing
This project is open to contributions. Feel free to raise an issue or submit a pull request.
  
# Conclusion
This code provides a convenient way to download YouTube videos and audio using Python. With the use of the **pytube **library and **ffmpeg **command line tool, the script makes it easy to download high-quality videos and audio files from YouTube.
