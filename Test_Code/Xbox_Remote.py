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
        if ID == "311" and val == "01":
             print("Right Bumper")
                  
      
        
        
    #Gamepad analogique | Analog gamepad
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        print ("Full", ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value)
        ecode = ecodes.bytype[absevent.event.type][absevent.event.code]
        print("ecode", ecode)
        Value = absevent.event.value
        print("Value", Value)

#         print(event)
#         print(type(event))
        ecodes_full = ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value
        string_ecode = str(ecodes_full)
        ID_ecode = string_ecode[2:11]
        print ("ID_ecode",ID_ecode)
        val_ecode = string_ecode[12:16]
        print("val_ecode",val_ecode)
        
        ## D-Pad
        if ID_ecode == "ABS_HAT0Y" and val_ecode == "-1":
             print("D-Pad Up",)
        if ID_ecode == "ABS_HAT0X" and val_ecode == "1":
             print("D-Pad Right")      
        if ID_ecode == "ABS_HAT0X" and val_ecode == "-1":
             print("D-Pad Left",)
        if ID_ecode == "ABS_HAT0Y" and val_ecode == "1":
             print("D-Pad Down")
             
             
             
    #print (xbox_input)
        
        
#         if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
#             if absevent.event.value < 30000:
#                 print("Left Stick Up",absevent.event.value)
#             if absevent.event.value > 30000:
#                 print("Left Stick down",absevent.event.value) 