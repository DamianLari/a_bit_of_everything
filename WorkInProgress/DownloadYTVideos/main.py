from pytube import YouTube
import argparse

def download_youtube_video(url, resolution='720p'):
    yt = YouTube(url)
    
    stream = yt.streams.filter(res=resolution, progressive=True, file_extension='mp4').first()
    
    if not stream:
        print(f"Resolution {resolution} not available, downloading the highest available resolution.")
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    
    if stream:
        stream.download()
        print(f"Video downloaded successfully: {yt.title}")
    else:
        print("Failed to find a suitable stream to download.")

parser = argparse.ArgumentParser(description='Download a YouTube video.')
parser.add_argument('video_url', help='URL of the YouTube video to download')
parser.add_argument('--resolution', default='720p', help='Resolution of the video to download (e.g., 720p, 1080p)')
args = parser.parse_args()

download_youtube_video(args.video_url, args.resolution)
