# YouTube Downloader Script

This script allows you to download videos, audio, and subtitles from YouTube playlists or single videos. It uses the `yt-dlp` library for downloading content.

## Prerequisites

- Python 3.x
- `yt-dlp` library
  

    pip install yt-dlp

## Installation

1. **Clone the Repository**:
    git clone https://github.com/YourUsername/YourRepositoryName.git


## Usage

You can download videos, audio, or subtitles from YouTube playlists or single videos using this script. The downloads are available in MP4 (video) and MP3 (audio) formats. All videos from a playlist will be downloaded if you choose the playlist option.

### Download  Playlist

To download videos, audio, or subtitles from a playlist, run the script and follow the prompts:

1. **Run the Script**:
    
    python playlist.py
    

2. **Choose Option**:
    - Enter `1` for Playlist
    - Enter `2` for Video

3. **For Playlist**:
    - Enter the playlist URL.
    - Choose format:
        - `1` for Videos
        - `2` for Audio
        - `3` for Subtitles

### Download Single Video

To download videos, audio, or subtitles from a single video:

1. **Run the Script**:
    ```bash
    python playlist.py
    ```

2. **Choose Option**:
    - Enter `2` for Video

3. **For Single Video**:
    - Enter the video URL.
    - Choose format:
        - `1` for Videos
        - `2` for Audio
        - `3` for Subtitles


## Notes

- All playlist videos will be downloaded when selecting the playlist option.
- Download paths are set to the current working directory by default.
- Ensure you have write permissions for the directory where you want to save files.
