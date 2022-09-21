#import evdev
from evdev import InputDevice, categorize, ecodes

#cree un objet gamepad | creates object gamepad
gamepad = InputDevice('/dev/input/event8')

#affiche la liste des device connectes | prints out device info at start
print(gamepad)
xbox_input= "null"
#affiche les codes interceptes |  display codes
for event in gamepad.read_loop():
    #Boutons | buttons 
    if event.type == ecodes.EV_KEY:
        #print("this is an event", event)
        #print(type(event))
        string = str(event)
        ID = string[33:36]
        val = string[51:54]
        #print("ID", ID)
        #print("val", val)
        
        ## Buttons
        if ID == "307" and val == "01":
             print("X")
             xbox_input = "X"
        if ID == "308" and val == "01":
             print("Y")
             xbox_input = "Y"
        if ID == "304" and val == "01":
             print("A")
             xbox_input = "A"
        if ID == "305" and val == "01":
             print("B")
             xbox_input = "B"
             
        ## View/Menu
        if ID == "158" and val == "01":
             print("View",)
             xbox_input = "View"
        if ID == "315" and val == "01":
             print("Menu")
             xbox_input = "Menu"
             
        ## Bumpers
        if ID == "310" and val == "01":
             print("Left Bumper",)
             xbox_input = "Left Bumper"
        if ID == "311" and val == "01":
             print("Right Bumper")
             xbox_input = "Right Bumper"