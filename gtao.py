import argparse

from src.macros.idle import main as idle

TITLE = "GTA Online Macro Script"

OPTIONS = {"idle": idle}

METHODS = ["keyboard", "gamepad"]

parser = argparse.ArgumentParser("gtao.py", description=TITLE)
parser.add_argument(
    "action",
    choices=list(OPTIONS.keys()),
    help="Action for the script to run, i.e. Idle Script",
)
parser.add_argument(
    "-m",
    "--method",
    choices=METHODS,
    help="Input method to use, i.e. Keyboard/Controller",
)

# Start main script
if __name__ == "__main__":

    try:
        # Parse command-line arguments
        arguments = parser.parse_args()

        print(f"Starting {TITLE} ...")

        # Run the script for the option
        result = OPTIONS[arguments.action](arguments.method)
    except Exception as e:
        print(f"Failed to start {TITLE}! {e}")
