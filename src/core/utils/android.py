import os
import subprocess
from core.utils import color

def upload_audio(filename, path, dest):
	subprocess.call([
		'adb', 'push', os.path.join(path, filename), dest
	])
	os.remove(os.path.join(path, filename))
	color.display_messages('audio file uploaded', success=True)