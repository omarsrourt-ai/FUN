from pyfirmata import Arduino, util
import time
import speech_recognition as sr
import pyttsx3



        
# -------------------------
# Setup PyFirmata
# -------------------------

print ('good')
board = Arduino('COM7')  

# Start iterator thread
it = util.Iterator(board)
it.start()


print ('hi')
# Setup servo pins
servo_pins = {
    'thumb': board.get_pin('d:2:s'),
    'index': board.get_pin('d:3:s'),
    'middle': board.get_pin('d:4:s'),
    'ring': board.get_pin('d:5:s'),
    'pinky': board.get_pin('d:6:s')
 }
print ('bye')

# Allow time to initialize
time.sleep(1)

# -------------------------
# Voice & TTS Setup
# -------------------------
r = sr.Recognizer()
engine = pyttsx3.init()

# -------------------------
# Functions to move servos
# -------------------------
def grab_obj():
    engine.say("Grabbing object now")
    engine.runAndWait()
    for pin in servo_pins.values():
        pin.write(0)  # close all fingers
    print("All fingers closed.")

def let_go():
    engine.say("Releasing now")
    engine.runAndWait()
    for pin in servo_pins.values():
        pin.write(180)  # open all fingers to 180 degrees
    
    for name, pin in servo_pins.items():
        if name == 'thumb':
            pin.write(0)  # point
    print("All fingers opened.")

def point_at():
    engine.say("Pointing")
    engine.runAndWait()
    # Close all fingers except index
    for name, pin in servo_pins.items():
        if name == 'index' or name == 'thumb':
            pin.write(180)  # point
        else:
            pin.write(0)  # close others
    print("Point gesture made.")

def thumbs_up():
    engine.say("Thumbs up")
    engine.runAndWait()
    for name, pin in servo_pins.items():
        if name == 'thumb':
            pin.write(0)  # thumb up
        else:
            pin.write(0)  # close others
    print("Thumbs up gesture made.")

def gun():
    engine.say("Pistol gesture")
    engine.runAndWait()
    for name, pin in servo_pins.items():
        if name in ['index']:
            pin.write(180)  # thumb & index out
        else:
            pin.write(0)
    print("Pistol gesture made.")


def ring():
    for name, pin in servo_pins.items():
        if name == 'ring':
            pin.write(180)  # ring finger out
    
def middle_fing():
    engine.say("Angry gesture")
    engine.runAndWait()
    for name, pin in servo_pins.items():
        if name == 'middle' or name == 'thumb':
            pin.write(180)  # middle finger out
        else:
            pin.write(0)
    print("Angry gesture made.")

# -------------------------
# Main listening function
# -------------------------
def main_func():
    
    
        
    while True:
        with sr.Microphone() as source:
            print("Say a word:")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said:", text)

            if "grab" in text.lower():
                grab_obj()
            elif "let go" or "let's go"in text.lower():
                let_go()
            elif "see that" in text.lower():
                point_at()
            elif "thumbs up" in text.lower():
                thumbs_up()
            elif "pistol" in text.lower():
                gun()
            elif "angry" in text.lower():
                middle_fing()

        except sr.UnknownValueError:
            print("Could not understand audio")

# -------------------------
# Test single function directly
# -------------------------
# let_go()
# thumbs_up()
# point_at()
# gun()
# middle_fing()
# grab_obj()

for name, pin in servo_pins.items():
    if name == 'thumb':
        pin.write(180)  # thumb up
main_func()
# ring()

# -------------------------
# Cleanup
# -------------------------
# board.exit()  # Call when done to cleanly close the connection
