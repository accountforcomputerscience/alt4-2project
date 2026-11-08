from settings import INPUT_MODE

from hardware.keyboard import get_keyboard_inputs

def get_inputs():
    if INPUT_MODE == "keyboard":
        return get_keyboard_inputs()
    
    elif INPUT_MODE == "microbit":
        #put microbit function here
        pass

    else:
        raise ValueError("Invalid input")


