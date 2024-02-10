import streetcat_viewer
import pytchat
import conf
import _thread
from time import sleep

chat = pytchat.create(video_id=input())
command = "ffmpeg -re -i"
parameters = "-pix_fmt yuvj420p -x264-params keyint=48:min-keyint=48:scenecut=-1 -b:v 4500k -b:a 128k -ar 44100 -acodec aac -vcodec libx264 -preset medium -crf 28 -threads 4 -f flv rtmp://a.rtmp.youtube.com/live2/" + conf.rtmp_key

def checker():
    while True:
        if streetcat_viewer.cam_proc is None or streetcat_viewer.cam_proc.poll() is not None:
            print("Cams Rebooting...")
            streetcat_viewer.play(command = command, 
                                parameters = parameters,
                                use_text = True,
                                fontfile = conf.fontfile)
        streetcat_viewer.cam_proc.wait()
        sleep(5)

_thread.start_new_thread(checker, ())

while chat.is_alive():
    for c in chat.get().sync_items():
        if c.message.split()[0] == "!camera":
            com, cam_name, cam_number = c.message.split()
            player = streetcat_viewer.play(command = command, 
                                parameters = parameters, 
                                cam_name = cam_name, 
                                cam_number = cam_number,
                                use_text = True,
                                fontfile = conf.fontfile)
            print(player[1])
        elif c.message.split()[0] == "!random":
            player = streetcat_viewer.play(command = command, 
                                parameters = parameters,
                                use_text = True,
                                fontfile = conf.fontfile)
            print(player[1])