import yt_dlp
import os

def download_playlist_videos(url, download_path):
    try:
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Playlist videos downloaded successfully!")
    except Exception as e:
        print(f"An error occurred while downloading the playlist videos: {e}")

def download_playlist_audio(url, download_path):
    try:
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Playlist audio downloaded successfully!")
    except Exception as e:
        print(f"An error occurred while downloading the playlist audio: {e}")

def download_playlist_subtitles(url, download_path):
    try:
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        ydl_opts = {
            'writesubtitles': True,
            'allsubtitles': True,
            'subtitlesformat': 'vtt',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Playlist subtitles downloaded successfully!")
    except Exception as e:
        print(f"An error occurred while downloading the playlist subtitles: {e}")

def download_videos(url_video, download_path):
    try:
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_video])

        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")

def download_audio(url_video, download_path):
    try:
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_video])

        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"An error occurred while downloading the audio: {e}")

def download_subtitles(url_video, download_path):
    try:
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        ydl_opts = {
            'skip_download': True,  # This ensures only subtitles are downloaded
            'writesubtitles': True,
            'allsubtitles': True,
            'subtitlesformat': 'vtt',  # You can change the format if needed
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_video])

        print("Subtitles downloaded successfully!")
    except Exception as e:
        print(f"An error occurred while downloading the subtitles: {e}")

# Set the download path to the current directory
download_path = os.getcwd()

# Prompt the user to choose between a playlist or a single video
print("Enter 1 for Playlist OR Enter 2 for Single Video: ")
video_or_playlist = int(input())

if video_or_playlist == 1:
    url_playlist = input('Enter playlist URL from YouTube: ')
    print("Which format do you want to download the playlist? Enter 1 for video, 2 for audio, 3 for subtitles : ")
    n = int(input())

    if n == 1:
        download_playlist_videos(url_playlist, download_path)
    elif n == 2:
        download_playlist_audio(url_playlist, download_path)
    elif n == 3:
        download_playlist_subtitles(url_playlist, download_path)
    else:
        print("Invalid option")

elif video_or_playlist == 2:
    url_video = input("Enter URL of the video: ")
    print("Enter 1 to download video, 2 to download audio, 3 to download subtitles: ")
    n = int(input())

    if n == 1:
        download_videos(url_video, download_path)
    elif n == 2:
        download_audio(url_video, download_path)
    elif n == 3:
        download_subtitles(url_video, download_path)
    else:
        print("Invalid option")
else:
    print("Invalid option")
