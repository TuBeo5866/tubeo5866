import os
import platform

# Define the custom resolution
width = 120
height = 40
title = "My Custom Terminal Window"

# Check the operating system
os_type = platform.system()

if os_type == "Windows":
    # For Windows, use the mode command to set the terminal size
    import msvcrt
    os.system(f"mode con: cols={width} lines={height}")
    os.system(f"title {title}")
    os.system(f'cls')
    print("Press any key to continue...")
    msvcrt.getch()

elif os_type in ["Linux", "Darwin"]:  # Darwin is for macOS
    # For Linux/macOS, use the stty command to set the terminal size
    import sys
    import termios
    import tty
    os.system(f"stty rows {height} cols {width}")
    os.system(f"printf '\033]0;{title}\a'")
    os.system(f'clear')
    print("Press any key to continue...")
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        sys.stdin.read(1)  # Wait for one character input
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)



