import subprocess
import os
import pytube
from src.core.utils import color

def get_playlist_videos(url):
	pl = pytube.Playlist(url)
	pl.populate_video_urls()
	return pl.video_urls

def select_video_streaming(url):
	yt = pytube.YouTube(url)
	return yt.streams.filter(subtype='mp4', progressive=True).order_by('resolution').asc().first()

def download_video(video_url, base_dir):
	video = select_video_streaming(video_url)
	color.display_messages('downloading video - {}'.format(video_url), info=True)
	video.download(base_dir)
	return video.default_filename

def mp4_to_mp3(filename, base_dir):
	color.display_messages('converting to mp3 - {}'.format(filename), info=True)

	subprocess.call([
		'ffmpeg', '-hide_banner', '-loglevel', 'error', '-i',
		os.path.join(base_dir, filename), 
		os.path.join(base_dir, filename[:-3]+'mp3')
	])

def download_audio(video_url, base_dir):
	try:
		filename = download_video(video_url, base_dir)
		mp4_to_mp3(filename, base_dir)
		os.remove(os.path.join(base_dir, filename))
		color.display_messages('audio downloaded succesfully', success=True)
	except Exception as e:
		color.display_messages('{} {}'.format(video_url, str(e)), error=True)
