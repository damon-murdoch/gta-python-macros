import time
import vgamepad as vg

# Joystick Coordinates
JOYSTICK_COORDINATES = {
    "up": 1.0,
    "down": -1.0,
    "left": -1.0,
    "right": 1.0,
    "neutral": 0,
}

# ~2s between inputs
SAVE_DELAY = 2

# ~4s input delay
INPUT_DELAY = 4

# ~8s between resets
RESET_DELAY = 6

# Single Button Press
SINGLE_PRESS = 0.1

# Sequence Button Press
SEQUENCE_PRESS = 0.5


def left_stick_and_release(gp, x, y, delay: int = SINGLE_PRESS):

    # Input the left joystick
    gp.left_joystick_float(x_value_float=x, y_value_float=y)
    gp.update()

    # Wait for delay (if set)
    if delay:
        time.sleep(delay)

    # Reset the left joystick
    gp.left_joystick_float(x_value_float=0, y_value_float=0)
    gp.update()


def press_and_release(gp, buttons, delay: int = SINGLE_PRESS):

    # Press button and update
    for button in buttons:
        gp.press_button(button=button)
    gp.update()

    # Wait for delay (if set)
    if delay:
        time.sleep(delay)

    # Release button and update
    for button in buttons:
        gp.release_button(button=button)
    gp.update()


def press_and_release_sequence(
    gp,
    sequence,
    delay_sequence: int = SEQUENCE_PRESS,
    delay_buttons: int = SINGLE_PRESS,
):

    # Loop over the sequence elements
    for buttons in sequence:
        # Press and release the buttons, wait for delay
        press_and_release(gp, buttons, delay_buttons)
        if delay_sequence:
            time.sleep(delay_sequence)


def get_gamepad():

    # Create virtual gamepad
    gp = vg.VX360Gamepad()

    return gp
