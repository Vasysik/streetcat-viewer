import subprocess
import random
from time import sleep
import urllib.request

fresh_1 = ["f_1", "http://streetcatpull.hellobike.com/live/4258783365322591678_0.m3u8", "http://streetcatpull.hellobike.com/live/4258783365322591678_1.m3u8", "http://streetcatpull.hellobike.com/live/4258783365322591678_2.m3u8"]
fresh_2 = ["f_2", "http://streetcatpull.hellobike.com/live/4412424173050749216_0.m3u8", "http://streetcatpull.hellobike.com/live/4412424173050749216_1.m3u8", "http://streetcatpull.hellobike.com/live/4412424173050749216_2.m3u8"]
sleeps = ["sl", "http://streetcatpull.hellobike.com/live/4489918405732275808_0.m3u8", "http://streetcatpull.hellobike.com/live/4489918405732275808_1.m3u8", "http://streetcatpull.hellobike.com/live/4489918405732275808_2.m3u8"]
snack = ["sn", "http://streetcatpull.hellobike.com/live/4291094747934800009_0.m3u8", "http://streetcatpull.hellobike.com/live/4291094747934800009_1.m3u8", "http://streetcatpull.hellobike.com/live/4291094747934800009_2.m3u8"]
shock = ["sh", "http://streetcatpull.hellobike.com/live/4584985755015398729_0.m3u8", "http://streetcatpull.hellobike.com/live/4584985755015398729_1.m3u8", "http://streetcatpull.hellobike.com/live/4584985755015398729_2.m3u8"]

cams = [fresh_1, fresh_2, sleeps, snack, shock]
cam_proc = None

def play(command = "ffplay", parameters = "", cam_name = "", cam_number = 1):
    cam_url = ""
    response = ""
    global cam_proc
    disabled = False
    for cam in cams:
        if str(cam_name) == str(cam[0]):
            cam_url = cam[int(cam_number)]

    if cam_url == "": cam_url = random.choice(cams)[random.randrange(1,4)]

    try: urllib.request.urlopen(cam_url)
    except: 
        disabled = True
        response = "Cam " + cam_name + " " + cam_number + " is disabled"

    if not disabled:
        if cam_proc:
            try:
                cam_proc.stdin.write('q'.encode('utf-8'))
                cam_proc.stdin.flush()
            except: None
        cam_proc = subprocess.Popen((command + " " + cam_url + " " + parameters), shell=True, stdin=subprocess.PIPE)

    return [cam_proc, response]
