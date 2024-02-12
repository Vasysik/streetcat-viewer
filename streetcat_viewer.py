import subprocess
import random
import time
import urllib.request
import json
import logging

with open('cams.json', 'r') as file:
    cams_json = file.read()
cams = json.loads(cams_json)
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
        cam_name =  random.choice(list(cams.keys()))
        cam_number = random.randrange(1, len(cams[cam_name]) + 1)
        response = f"Cam {cam_name} {cam_number} is turned on"
        cam_url = cams[cam_name][cam_number - 1]
        logging.info(f"{current_time()} | Rand {response} url: {cam_url}")
    else:
        if cam_name in cams and cams[cam_name]:
            if 1 <= cam_number <= len(cams[cam_name]):
                cam_url = cams[cam_name][cam_number - 1]
                logging.info(f"{current_time()} | {response} url: {cam_url}")
            else:
                disabled = True
                response = f"Cam {len(cams[cam_name])} does not exist - invalid number"
                logging.error(f"{current_time()} | {response}")
        else:
            disabled = True
            response = f"Cam {str(cam_name)} {str(cam_number)} does not exist - invalid name"
            logging.error(f"{current_time()} | {response}")

    if cam_url != "":
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
