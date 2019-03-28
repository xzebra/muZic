import subprocess
import os
import pytube

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

def download_video(video, base_dir):
	video.download(os.path.join(base_dir, 'downloads'))
	filename = video.default_filename
	subprocess.call([
		'ffmpeg', '-i', 
		os.path.join(base_dir, filename), 
		os.path.join(base_dir, filename[:-3]+'mp3')
	])
