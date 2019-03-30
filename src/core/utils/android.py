import os
import subprocess
from src.core.utils import color

def upload_audio(filename, path, dest):
	subprocess.call([
		'adb', 'push', os.path.join(path, filename), dest
	])
	color.display_messages('audio file uploaded', success=True)