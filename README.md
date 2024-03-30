# Key-Logger

This Python script is a simple keylogger designed to record keystrokes and save them into a log file. 

## For Linux

It utilizes the `pyxhook` library to monitor keyboard events.

## Features

- Records all key presses except for special keys such as Cancel, Backspace, Shift, Alt, and Control keys.
- Writes the recorded keystrokes into a log file (`file.log` by default) on the desktop.
- Clears the log file each time the script is executed.
- Special keys like Backspace, Shift, Alt, and Control are logged as `<backspace>`, `<shift>`, `<alt>`, and `<control>` respectively.

## Prerequisites

- Python 3.x installed on your system.
- `pyxhook` library installed. You can install it using pip:
  ```
  pip install pyxhook
  ```

## Usage

1. Save the provided Python script (`Key-Logger.py`) on your system.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using Python:
   ```
   python keylogger.py
   ```
4. The keylogger will start running silently in the background.
5. To stop the keylogger, press the cancel key (default is the backtick/backquote key `).

## Customization

- **Log File Path**: You can change the path of the log file by modifying the `log_file` variable in the script.
- **Cancel Key**: You can change the cancel key by modifying the `cancel_key` variable in the script. By default, it's set to the backtick/backquote key (`).

## For Windows

## Security and Privacy

- **Warning**: Please use this script responsibly and only on your own devices. Keyloggers can be considered intrusive and unethical if used without consent.
- **Privacy**: Ensure that you have the necessary permissions to monitor keystrokes on the target system. Respecting privacy laws and obtaining consent from users is essential.

## Disclaimer

This script is provided for educational purposes only. The author assumes no liability and is not responsible for any misuse or damage caused by this script. Use it at your own risk.

For any questions or concerns, please feel free to contact the author.

---
**Note:** Remember to adhere to legal and ethical guidelines when using this or any other monitoring tool. Always respect individuals' privacy and obtain proper authorization before deploying such software.

