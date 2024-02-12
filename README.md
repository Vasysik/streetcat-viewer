# StreetCat-viewer

# Installation guide:
1) Install [Python 3.10](https://www.python.org/downloads/)
2) Install [git](https://git-scm.com/downloads)
3) Install [ffmpeg](https://ffmpeg.org/download.html)
4) Download the streetcat-viewer repository:
   ```
   git clone https://github.com/Vasysik/streetcat-viewer/
   cd .\streetcat-viewer\
   ```
5) Install all remaining required libraries:
   ```
   pip install -r requirements.txt
   ```
6) Create a file ```conf.py``` containing:
    ```
    # Font file location for text in FFMEG
    fontfile = "./CALIBRI.TTF"

    # Client keys for restream_youtube.py
    rtmp_key = ""
    client_id = ""
    client_secret = ""
    ```

# Functions:
Main library functions (streetcat_viewer.py):
1) Camera playback function:
   ```
   play(command, parameters, cam_name, cam_number, use_text, fontfile)
   ```
   The output is a list containing subprocess.Popen() and a response string.

Currently there are 2 programs for working with cameras:
1) console_viewer.py
2) restream_youtube.py

