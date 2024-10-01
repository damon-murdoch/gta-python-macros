import argparse

import sys, time
import vgamepad as vg

import src.macro as macro

TITLE = "GTA Online Macro Script"

OPTIONS = {
    "idle": macro.idle
}

parser = argparse.ArgumentParser("gtao.py", description=TITLE)
parser.add_argument("action", choices=list(OPTIONS.keys()))

# Start main script
if __name__ == "__main__":

    try: 
        # Parse command-line arguments
        arguments = parser.parse_args()

        print(f"Starting {TITLE} ...")

        # Run the script for the option
        result = OPTIONS[arguments.action]()
    except Exception as e:
        print(f"Failed to start {TITLE}! {e}")