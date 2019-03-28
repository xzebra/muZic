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
This will keep your configuration stored in a .ini file

- Download audio given YouTube url:
```
:: download -l https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

## Requirements

- Python libraries:
  - pytube
  - configparser
  
- Other:
  - [ffmpeg](https://ffmpeg.org/)