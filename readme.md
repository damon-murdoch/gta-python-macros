# GTA Python Macros

### Created By Damon Murdoch ([@SirScrubbington](https://github.com/SirScrubbington))

## Description

This script automates idle actions in GTA Online, simulating periodic inputs to keep the player from being disconnected due to inactivity. It includes methods for both keyboard and gamepad input, ideal for AFK farming in safe locations within the game. The script can simulate idle actions like moving forward briefly or pressing buttons at set intervals.

## Table of Contents

- [Live Demo](#live-demo)
- [Installation](#installation)
- [Usage](#usage)
- [Future Changes](#future-changes)
- [Problems / Improvements](#problems--improvements)
- [Changelog](#changelog)
- [Sponsor this Project](#sponsor-this-project)
- [License](#license)

## Live Demo

No live demo is available for this project.

## Installation

To install and set up this script, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/damon-murdoch/gta-python-macros
   cd gta-python-macros
   ```

2. **Install Dependencies**:
   Install the required libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Additional Modules**:
   - Ensure that `vgamepad` and `keyboard` modules are correctly configured, as they are used for simulating inputs.

## Usage

The script can be run with `action` and optional input `method` arguments to specify idle mode and input type.

1. **Basic Command**:
   ```bash
   python gtao.py idle --method keyboard
   ```

   - `action`: Specifies the action to run, e.g., `idle`.
   - `method`: Specifies the input method (`keyboard` or `gamepad`).

2. **Example Usage for Gamepad**:
   ```bash
   python gtao.py idle -m gamepad
   ```

## Future Changes

Plans for potential improvements:

| Change Description                     | Priority |
| -------------------------------------- | -------- |
| Add support for additional macros      | High     |
| Add configuration for custom intervals | Medium   |

## Problems / Improvements

For issues or improvement suggestions, please open an [issue on GitHub](../../issues) or reach out on Twitter with details of the issue and steps to replicate it.

## Changelog

List of changes across versions:

### Ver. 0.1.1

Added readme, license file

### Ver. 0.1.0
Initial release with basic idle actions for keyboard and gamepad.

## Sponsor this Project

If you'd like to support the development of this and future projects, feel free to contribute through [PayPal](https://www.paypal.com/paypalme/sirsc).

## License

Distributed under the MIT License. See `LICENSE` for more information.
