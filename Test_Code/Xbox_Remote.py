#import evdev
from evdev import InputDevice, categorize, ecodes

#cree un objet gamepad | creates object gamepad
gamepad = InputDevice('/dev/input/event2')

#affiche la liste des device connectes | prints out device info at start
print(gamepad)

#affiche les codes interceptes |  display codes
for event in gamepad.read_loop():
    #Boutons | buttons 
    if event.type == ecodes.EV_KEY:
        print("this is an event", event)
        print(type(event))
        string = str(event)
        ID = string[33:36]
        print("ID", ID)
        if ID == "307":
             print("X")
        if ID == "308":
             print("Y")
        if ID == "304":
             print("A")
        if ID == "305":
             print("B")
      
        
        
    #Gamepad analogique | Analog gamepad
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        print ("Full", ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value)
        print("ecode", ecodes.bytype[absevent.event.type][absevent.event.code])
        print("Value", absevent.event.value)
        
        
        
        
        
#         if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
#             if absevent.event.value < 30000:
#                 print("Left Stick Up",absevent.event.value)
#             if absevent.event.value > 30000:
#                 print("Left Stick down",absevent.event.value) 
