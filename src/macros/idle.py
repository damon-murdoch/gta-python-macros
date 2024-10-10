import time
import keyboard
import src.gamepad as gamepad

# from vgamepad import XUSB_BUTTON as button
from src.gamepad import JOYSTICK_COORDINATES as joystick

# Sleep between sequences
# Inputs completed once per minute
IDLE_SLEEP = 60


def input_gp(gp, delay=IDLE_SLEEP):
    # Flick left on the left stick (Walk forwards)
    gamepad.left_stick_and_release(gp, joystick["neutral"], joystick["up"])
    time.sleep(delay)


def input_kb(delay=IDLE_SLEEP):
    # Press 'w' on the keyboard
    keyboard.press_and_release("w")
    time.sleep(delay)


def idle_gp():

    print(
        "Please ensure no controllers are connected, and inputs are not captured by another window (i.e. Virtual Machines)."
    )

    print(
        f"The left stick will be moved every {IDLE_SLEEP} seconds for a brief moment."
    )

    # Create new gamepad
    gp = gamepad.get_gamepad()

    i=0
    # Input Loop
    while True:
        print(f"Input Loop: {i} ...")
        input_gp(gp)
        i+=1


def idle_kb():

    print(
        "Please ensure the GTA Online window is focused, and inputs are not captured by another window (i.e. Virtual Machines)."
    )

    print(
        f"The forward key (W) will be pressed every {IDLE_SLEEP} seconds for a brief moment."
    )

    i=0
    # Input Loop
    while True:
        print(f"Input Loop: {i} ...")
        input_kb()
        i+=1

# Scripts
METHODS = {"keyboard": idle_kb, "gamepad": idle_gp}


def main(method):

    print(f"Starting GTA Online Idle Script ({method} mode) ...")

    print(
        "Note: This script is best used while standing at the open safe in the Night Club / Agency."
    )

    # Run method script
    METHODS[method]()
