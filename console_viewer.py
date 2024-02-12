import streetcat_viewer
import conf

while(True):
    print("Cats Cams:")
    print(" Mr Fresh: fresh")
    print(" Mr Despair: despair")
    print(" Miss Sleeps: sleeps")
    print(" Mr Snack: snack")
    print(" Mr Shock: shock")
    print(" Mr Sonic: sonic")
    print(" Ducks: ducks")
    
    print("Enter camera name: ", end="")
    cam_name = input()
    print("Cam number: ", end="")
    cam_number = input()

    player = streetcat_viewer.play(command = "ffplay", 
                        parameters = "", 
                        cam_name = cam_name, 
                        cam_number = int(cam_number),
                        use_text = True,
                        fontfile = conf.fontfile)
    player[0].wait()
    print(player[1])