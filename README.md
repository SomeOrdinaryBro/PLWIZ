
# PLWIZ - YouTube and Instagram Video Downloader

PLWIZ is a Python script that allows you to download videos from YouTube and Instagram using the pytube library and ffmpeg command line tool.

## Requirements

1.  [Python](https://www.python.org/) 3.x (Latest)
2.  [pytube](https://github.com/nficano/pytube) library
3.  [ffmpeg](https://www.ffmpeg.org/) command line tool

## Usage

To use the script, you need to install the required libraries and tools. The pytube library can be installed using the following command:

`pip install pytube`

The ffmpeg command line tool can be installed using the package manager of your operating system.

Once you have installed the required libraries and tools, you can run the script using the following command:

`python plwiz.py`

## Features

### YouTube Video/Audio Downloader

PLWIZ allows you to download either the audio or video of a YouTube video. The audio_downloader function downloads the audio of a given YouTube video and saves it as an MP3 file, while the video_downloader function downloads the video and saves it as an MP4 file. The script also includes the is_valid_url function, which checks if a given URL is a valid YouTube URL.

### Instagram Video Downloader

PLWIZ also allows you to download videos from Instagram. The function insta_downloader takes a URL of an Instagram video and downloads the video to your local machine.

### Usage instructions

-   Once you run the script, you will be prompted to enter a URL.
-   If the URL is valid, you will be asked to choose between downloading audio or video (for YouTube videos).
-   If you choose to download audio, the audio file will be saved in the current directory as an MP3 file.
-   If you choose to download video, you will be prompted to choose the desired quality (360p, 480p, 720p, or 1080p) and the video file will be saved in the current directory as an MP4 file.

## How to run?

-   Clone the repository
-   Install the required libraries and tools
-   Run the script using the command `python plwiz.py`
-   Enter the URL of the YouTube or Instagram video you want to download.
-   Follow the instructions on the screen to download either audio or video.

## Contributing

This project is open to contributions. Feel free to raise an issue or submit a pull request.

## Conclusion

PLWIZ provides a convenient way to download videos from YouTube and Instagram using Python. With the use of the pytube library and ffmpeg command line tool, the script makes it easy to download high-quality videos and audio files.
