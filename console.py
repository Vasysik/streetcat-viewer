import streetcat_viewer

while(True):
    print("Cats Cams:")
    print(" Mr Fresh: f_1 or f_2")
    print(" Miss Sleeps: sl")
    print(" Mr Snack: sn")
    print(" Mr Shock: sh")
    
    print("Enter camera name: ", end="")
    cam_name = input()
    cam_url = ""

    for cam in streetcat_viewer.cams:
        if cam_name == cam[0]:
            print("Cam number: ", end="")
            cam_url = cam[int(input())]
    streetcat_viewer.play(command = "ffplay", parameters = "", cam_url = cam_url)