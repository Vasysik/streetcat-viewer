import subprocess
import random
from time import sleep

fresh_1 = ["f_1", "http://streetcatpull.hellobike.com/live/4258783365322591678_0.m3u8", "http://streetcatpull.hellobike.com/live/4258783365322591678_1.m3u8", "http://streetcatpull.hellobike.com/live/4258783365322591678_2.m3u8"]
fresh_2 = ["f_2", "http://streetcatpull.hellobike.com/live/4412424173050749216_0.m3u8", "http://streetcatpull.hellobike.com/live/4412424173050749216_1.m3u8", "http://streetcatpull.hellobike.com/live/4412424173050749216_2.m3u8"]
sleeps = ["sl", "http://streetcatpull.hellobike.com/live/4489918405732275808_0.m3u8", "http://streetcatpull.hellobike.com/live/4489918405732275808_1.m3u8", "http://streetcatpull.hellobike.com/live/4489918405732275808_2.m3u8"]
snack = ["sn", "http://streetcatpull.hellobike.com/live/4291094747934800009_0.m3u8", "http://streetcatpull.hellobike.com/live/4291094747934800009_1.m3u8", "http://streetcatpull.hellobike.com/live/4291094747934800009_2.m3u8"]
shock = ["sh", "http://streetcatpull.hellobike.com/live/4584985755015398729_0.m3u8", "http://streetcatpull.hellobike.com/live/4584985755015398729_1.m3u8", "http://streetcatpull.hellobike.com/live/4584985755015398729_2.m3u8"]

cams = [fresh_1, fresh_2, sleeps, snack, shock]
cam_proc = None

def play(command = "ffplay", parameters = "", cam_name = "", cam_number = 1):
    cam_url = ""
    for cam in cams:
        if str(cam_name) == str(cam[0]):
            cam_url = cam[int(cam_number)]

    if cam_url == "": cam_url = random.choice(cams)[random.randrange(1,4)]

    global cam_proc
    if cam_proc: cam_proc.terminate()
    cam_proc = subprocess.Popen(command + " " + cam_url + " " + parameters)
    return cam_proc
