import time
import src.gamepad as gamepad

# from vgamepad import XUSB_BUTTON as button
from src.gamepad import JOYSTICK_COORDINATES as joystick

# Sleep between sequences
# Inputs completed once per minute
IDLE_SLEEP = 30


def idle():

    # Input Loop
    def input_loop(gp, loops, sleep=IDLE_SLEEP):

        # New loops value
        new_loops = loops + 1

        print(f"Starting input loop {new_loops} ...")

        # Flick left on the left stick (change pose on seat)
        gamepad.left_stick_and_release(gp, joystick["left"], joystick["neutral"])

        # Wait 'sleep' seconds
        time.sleep(sleep)

        print("Done.")

        return new_loops

    # Create new gamepad
    gp = gamepad.get_gamepad()

    print(
        "Please ensure no controllers are connected, and inputs are not captured by another window (i.e. Virtual Machines)."
    )

    print(
        f"The left stick will be moved every {IDLE_SLEEP} seconds for a brief moment."
    )

    print(
        "Note: This script is best used while sitting at the lounge in the Bail Office / Night Club."
    )

    # Loop Counter
    loops = 0

    # Infinite loop
    while True:
        # Perform the input loop
        loops = input_loop(gp, loops)
