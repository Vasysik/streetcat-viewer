import subprocess
import random
import time
import urllib.request
import logging

fresh = ["fresh", "http://streetcatpull.hellobike.com/live/4258783365322591678_0.m3u8", "http://streetcatpull.hellobike.com/live/4258783365322591678_1.m3u8", "http://streetcatpull.hellobike.com/live/4258783365322591678_2.m3u8"]
despair = ["despair", "http://streetcatpull.hellobike.com/live/4412424173050749216_0.m3u8", "http://streetcatpull.hellobike.com/live/4412424173050749216_1.m3u8", "http://streetcatpull.hellobike.com/live/4412424173050749216_2.m3u8"]
sleeps = ["sleeps", "http://streetcatpull.hellobike.com/live/4489918405732275808_0.m3u8", "http://streetcatpull.hellobike.com/live/4489918405732275808_1.m3u8", "http://streetcatpull.hellobike.com/live/4489918405732275808_2.m3u8"]
snack = ["snack", "http://streetcatpull.hellobike.com/live/4291094747934800009_0.m3u8", "http://streetcatpull.hellobike.com/live/4291094747934800009_1.m3u8", "http://streetcatpull.hellobike.com/live/4291094747934800009_2.m3u8"]
shock = ["shock", "http://streetcatpull.hellobike.com/live/4584985755015398729_0.m3u8", "http://streetcatpull.hellobike.com/live/4584985755015398729_1.m3u8", "http://streetcatpull.hellobike.com/live/4584985755015398729_2.m3u8"]
sonic = ["sonic", "http://streetcatpull.hellobike.com/live/4303090694701059290_0.m3u8", "http://streetcatpull.hellobike.com/live/4303090694701059290_1.m3u8", "http://streetcatpull.hellobike.com/live/4303090694701059290_2.m3u8"]
ducks = ["ducks", "http://streetcatpull.hellobike.com/live/4300845904274638881_0.m3u8", "http://streetcatpull.hellobike.com/live/4300845904274638881_1.m3u8", "http://streetcatpull.hellobike.com/live/4300845904274638881_2.m3u8"]

cams = [fresh, despair, sleeps, snack, shock, sonic, ducks]
cam_proc = None

def current_time():
    return time.strftime("%H:%M:%S", time.localtime())

def play(command = "ffplay", parameters = "", cam_name = "", cam_number = 1, use_text = False, fontfile = ""):
    logging.info(f"{current_time()} | Play {command} {parameters} {cam_name} {cam_number} {use_text} {fontfile}")
    cam_url = ""
    response = f"Cam {cam_name} {cam_number} is turned on"
    text = ""
    global cam_proc
    disabled = False
    
    if cam_name == "": 
        cam = random.choice(cams)
        cam_name = cam[0]
        cam_number = random.randrange(1,4)
        response = f"Cam {cam_name} {cam_number} is turned on"
        cam_url = cam[cam_number]
        logging.info(f"{current_time()} | Rand {response} url: {cam_url}")
    else:
        for cam in cams:
            if str(cam_name) == str(cam[0]):
                cam_url = cam[int(cam_number)]
                logging.info(f"{current_time()} | {response} url: {cam_url}")

    if cam_url == "":
        disabled == True
        response = f"Cam {str(cam_name)} {str(cam_number)} does not exist"
        logging.error(f"{current_time()} | {response}")
    else:
        try: urllib.request.urlopen(cam_url)
        except: 
            disabled = True
            response = f"Cam {str(cam_name)} {str(cam_number)} is disabled"
            logging.error(f"{current_time()} | {response} url: {cam_url}")

    if use_text: text = f"-vf \"drawtext=fontfile={str(fontfile)}:fontsize=18:fontcolor=white:fontsize=24:box=1:boxcolor=black@0.5:boxborderw=5:x=5:y=5:text='Camera\: {str(cam_name)} {str(cam_number)}'\""

    if not disabled:
        if cam_proc:
            try:
                logging.info(f"{current_time()} | FFMPEG killing...")
                cam_proc.stdin.write('q'.encode('utf-8'))
                cam_proc.stdin.flush()
                logging.info(f"{current_time()} | FFMPEG killed successfully!")
            except: logging.error(f"{current_time()} | FFMPEG killing ERROR")
        try:
            logging.info(f"{current_time()} | FFMPEG launch: {command} {cam_url} {text} {parameters}")
            cam_proc = subprocess.Popen(f"{command} {cam_url} {text} {parameters}", shell=True, stdin=subprocess.PIPE)
        except: logging.error(f"{current_time()} | FFMPEG launch ERROR")

    return [cam_proc, response]
