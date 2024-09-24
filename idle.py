import sys, time
import vgamepad as vg


def press_button(gp, button, duration=None):

    # Press the button
    gp.press_button(button=button)
    gp.update()

    print(f"Button '{button}' pressed.")

    # Duration set
    if duration:

        # Wait 'duration' seconds
        time.sleep(duration)

        # Release the button
        gp.release_button(button=button)
        gp.update()

        print(f"Button '{button}' released.")


def run_idle(sleep: int = 5, duration: int | None = None):

    # Loop Counter
    loops = 0

    print("Starting virtual gamepad service ...")

    # Create new gamepad
    gp = vg.VX360Gamepad()

    # Loop infinitely, or until 'duration' loops
    while (duration == None) or (loops < duration):

        press_button(gp, vg.XUSB_BUTTON.XUSB_GAMEPAD_A, 1)

        # Sleep 'n' seconds
        time.sleep(sleep)

    print("Virtual gamepad service stopped.")


# Start main script
if __name__ == "__main__":

    # 5s between inputs
    delay = 5

    # Run for 'duration' loops
    duration = None

    # Get the arguments
    args = sys.argv[1:]

    # Any arguments
    if len(args) > 0:
        # Read first arg as int
        delay = int(args[0])

        print(f"Delay set to: {delay} seconds.")

        # Second argument
        if len(args) > 1:
            # Read second arg as int
            duration = int(args[1])

            print(f"Duration set to: {duration} iterations.")

    # Run idle script
    run_idle(delay)
