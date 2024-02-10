import streetcat_viewer

while(True):
    print("Cats Cams:")
    print(" Mr Fresh: f_1 or f_2")
    print(" Miss Sleeps: sl")
    print(" Mr Snack: sn")
    print(" Mr Shock: sh")
    
    print("Enter camera name: ", end="")
    cam_name = input()
    print("Cam number: ", end="")
    cam_number = input()

    try: 
        player = streetcat_viewer.play(command = "ffplay", 
                            parameters = "", 
                            cam_name = cam_name, 
                            cam_number = cam_number)
        player[0].wait()
        print(player[1])
    except: print("Player Error")