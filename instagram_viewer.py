import webbrowser
import re
import json
import requests
from bs4 import BeautifulSoup


def open_instagram_video(post_url):
    response = requests.get(post_url, timeout=5)
    soup = BeautifulSoup(response.content, 'html.parser')

    is_private = soup.find('meta', property='og:private')
    if is_private and is_private['content'] == "True":
        print("Error: Video is from a private profile and cannot be opened.")
        return

    is_public = soup.find('meta', property='og:visibility')
    if is_public and is_public['content'] == "private":
        print("Error: This is a private post and cannot be opened.")
        return

    script_tag = soup.find('script', string=re.compile(r'window\.__additionalDataLoaded'))
    if script_tag:
        json_data = script_tag.string.strip().replace(
            'window.__additionalDataLoaded(\'feed\',', '')[:-1]
        data = json.loads(json_data)
        if 'graphql' in data:
            media = data['graphql']['shortcode_media']
            if media['is_video']:
                video_url = media['video_url']
                webbrowser.open(video_url)
            else:
                print("Error: This post does not have a video.")
        elif 'entry_data' in data and 'PostPage' in data['entry_data']:
            media = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
            if media['is_video']:
                video_url = media['video_url']
                webbrowser.open(video_url)
            else:
                print("Error: This post does not have a video.")
        else:
            print("Error: Could not find video data in response.")
    else:
        print("Error: Script tag containing JSON data not found. Please try again later.")


url = input("Enter an Instagram video URL: ")

if "instagram.com/p/" in url or "instagram.com/reel/" in url:
    open_instagram_video(url)
else:
    print("Invalid Instagram post URL.")
