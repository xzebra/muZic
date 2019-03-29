import subprocess
import os
import pytube
from core.utils import color

def select_video_streaming(url):
	yt = pytube.YouTube(url)

	# list all possible streamings
	vids = yt.streams.all()
	# select the lowest res possible
	lowest = -1
	for i in range(len(vids)):
		if vids[i].mime_type == 'video/mp4':
			if lowest == -1 or str(vids[i].res) < str(vids[lowest].res):
				lowest = i
    
	return vids[lowest]

def download_audio(video, base_dir):
	color.display_messages('downloading video', info=True)
	video.download(os.path.join(base_dir))
	filename = video.default_filename
	color.display_messages('converting to mp3', info=True)
	print(os.path.join(base_dir, filename), os.path.join(base_dir, filename[:-3]+'mp3'))
	subprocess.call([
		'ffmpeg', '-hide_banner', '-loglevel', 'panic', '-i',
		os.path.join(base_dir, filename).replace('&', '"&"'), 
		os.path.join(base_dir, filename[:-3]+'mp3').replace('&', '"&"')
	])
	os.remove(os.path.join(base_dir, filename))
	color.display_messages('audio downloaded succesfully', success=True)
