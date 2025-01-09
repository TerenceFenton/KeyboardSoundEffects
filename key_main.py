from pynput import keyboard
from pydub import AudioSegment
from pydub.playback import play
import thread
import time


# Global Objects
general_thread_used = False
return_thread_used = False
backspace_thread_used = False
end_thread_resetter = False


# Sound Conditionals:
def play_backspace_sound():

    # Sound file
    backspace_key = 'output2025-01-09 16:53:31.mp3' # Bup^

    # Play sound
    sound = AudioSegment.from_mp3(backspace_key)
    play(sound)


def play_return_sound():
    # Sound file
    return_key = 'output2025-01-09 16:54:26.mp3' # Shwoop

    # Play sound
    sound = AudioSegment.from_mp3(return_key)
    play(sound)


def play_general_sound():
    # Sound file
    general_key = 'output2025-01-09 16:52:18.mp3' # Bup

    # Play sound
    sound = AudioSegment.from_mp3(general_key)
    play(sound)


# Func to play sounds from listener
def play_key_input(input):
    # Globals
    global backspace_thread_used
    global return_thread_used
    global general_thread_used
    global end_thread_resetter


    # Conditions
    if input == keyboard.Key.backspace:
        backspace_thread.start()
        backspace_thread_used = True

    elif input == keyboard.Key.enter:
        return_thread.start()
        return_thread_used = True

    elif input == keyboard.Key.esc:
        end_thread_resetter = True
        return False
    
    else:
        general_thread.start()
        time.sleep(0.01)
        general_thread_used = True


# Thread Setup
backspace_thread = thread.Thread(target=play_backspace_sound)
return_thread = thread.Thread(target=play_return_sound)
general_thread = thread.Thread(target=play_general_sound)

# Thread resetter
def thread_ressetter():
    # Globals
    global end_thread_resetter
    global backspace_thread
    global return_thread
    global general_thread

    while end_thread_resetter is False:
        if backspace_thread_used is True:
            backspace_thread = thread.Thread(target=play_backspace_sound)
        if return_thread_used is True:
            return_thread = thread.Thread(target=play_return_sound)
        if general_thread_used is True:
            general_thread = thread.Thread(target=play_general_sound)
        

# Listener setup & Main
thread_ressetter_thread = thread.Thread(target=thread_ressetter)
thread_ressetter_thread.start()
print('Program has Started')
with keyboard.Listener(on_press=play_key_input) as listener:
    listener.join()

thread_ressetter_thread.join()
