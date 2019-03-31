# muZic

Download audio from YouTube and store it in the desired path

## How to use

- General help:
```
:: help
```

- Specific help:
```
:: config -h
```

- Configure download path (requires an existing folder and writing rights):
```
:: config -p ../test
```

- Download audio given YouTube url:
```
:: download https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

- Download playlist given YouTube url:
```
:: download https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLSM9Rzy5Qpq2YxoLqV0LxW-h3igLGFNx9 --playlist
```

- Upload audio files to android device:
```
:: upload
```

## How to install

```
$ python ./setup.py install
```

## Requirements

Python 3 or greater versions

You can get the python libraries listed below by doing
```
$ pip install -r < requirements.txt
```

- Python libraries:
    - pytube
    - configparser
    - colorama
  
ADB is only required if the destination device is an android smartphone,
otherwise you can set the download folder to drop files on other device.

- Other:
    - [ffmpeg](https://ffmpeg.org/)
    - [adb](https://developer.android.com/studio/command-line/adb)